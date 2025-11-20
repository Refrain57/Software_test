import requests
import time
import subprocess
import pytest

# 开关：如果你真的有 Docker MySQL 环境，设为 True
# 如果只是本地模拟 Flask 故障，设为 False (使用 app.py 里的模拟接口)
USE_DOCKER = False 

BASE_URL = "http://127.0.0.1:5000"

def simulate_db_failure(is_fail=True):
    """辅助函数：切断或恢复数据库"""
    if USE_DOCKER:
        action = "stop" if is_fail else "start"
        print(f"正在执行 Docker 命令: docker {action} mysql_db")
        subprocess.run(["docker", action, "mysql_db"], check=False)
    else:
        # 使用 app.py 提供的调试接口模拟
        state = False if is_fail else True
        requests.post(f"{BASE_URL}/debug/set_db_state", json={"connected": state})

def test_db_failure_recovery():
    """
    测试场景：数据库宕机后，系统应报错(500)；恢复后，系统应正常(200)。
    """
    print("\n[阶段 1] 正常下单测试...")
    res_normal = requests.post(f"{BASE_URL}/order", json={"item": "book", "qty": 1})
    assert res_normal.status_code in [200, 400] # 200成功或400库存不足都算服务正常

    print("[阶段 2] 模拟数据库故障 (断开连接)...")
    simulate_db_failure(is_fail=True)
    time.sleep(1) # 等待状态生效

    print("[阶段 3] 验证故障处理...")
    try:
        res_fail = requests.post(f"{BASE_URL}/order", json={"item": "book", "qty": 1})
        print(f"故障时响应状态码: {res_fail.status_code}")
        # 断言：系统应该识别出错，返回 500 或 503，而不是卡死
        assert res_fail.status_code in (500, 503)
    finally:
        # 无论测试是否通过，都要尝试恢复环境，否则后续测试全挂
        print("[阶段 4] 恢复数据库...")
        simulate_db_failure(is_fail=False)
        time.sleep(1)

    print("[阶段 5] 验证服务恢复...")
    res_recover = requests.post(f"{BASE_URL}/order", json={"item": "book", "qty": 1})
    assert res_recover.status_code in [200, 400]
    print("✅ 容错性测试通过：系统成功从数据库故障中恢复。")

if __name__ == "__main__":
    test_db_failure_recovery()