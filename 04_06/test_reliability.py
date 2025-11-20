import time
import requests

def test_reliability():
    """
    测试场景：连续高频请求下，系统是否稳定（不崩溃、不内存溢出）。
    """
    url = "http://127.0.0.1:5000/order"
    total_requests = 1000
    success_count = 0
    fail_count = 0 # 库存不足
    error_count = 0 # 系统错误

    print(f"🚀 开始可靠性测试，计划执行 {total_requests} 次请求...")
    start_time = time.time()

    for i in range(total_requests):
        try:
            res = requests.post(url, json={"item": "book", "qty": 1})
            
            # 逻辑判断
            if res.status_code == 200:
                success_count += 1
            elif res.status_code == 400:
                # 库存不足也是正常的业务逻辑返回
                fail_count += 1
            else:
                error_count += 1
                print(f"⚠️ 第 {i+1} 次请求异常: {res.status_code}")

            # 每 100 次打印一下进度
            if (i + 1) % 100 == 0:
                print(f"进度: {i + 1}/{total_requests}...")

        except Exception as e:
            error_count += 1
            print(f"请求发送失败: {e}")

    end_time = time.time()
    duration = end_time - start_time
    rps = total_requests / duration

    print("\n====== 可靠性测试报告 ======")
    print(f"运行时长: {duration:.2f} 秒")
    print(f"平均 RPS: {rps:.2f} req/s")
    print(f"成功订单: {success_count}")
    print(f"库存不足: {fail_count} (业务预期内)")
    print(f"系统错误: {error_count}")
    
    # 断言：系统错误率应为 0
    assert error_count == 0, f"测试失败，出现 {error_count} 个系统错误"
    print("✅ 可靠性测试通过：服务长时间运行稳定。")

if __name__ == "__main__":
    test_reliability()