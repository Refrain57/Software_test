import requests
import pytest

def test_sql_injection_attack():
    """
    测试 SQL 注入防御机制
    尝试使用万能钥匙 ' OR 1=1 -- 绕过登录
    """
    url = "http://127.0.0.1:5000/login"
    
    # 构造恶意 Payload
    # 意图：SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = 'xxx'
    payload = {
        "username": "' OR 1=1 --", 
        "password": "xxx"
    }
    
    print(f"\n正在发送恶意 Payload: {payload['username']}")
    
    try:
        res = requests.post(url, json=payload)
        
        print(f"服务器响应状态码: {res.status_code}")
        print(f"服务器响应内容: {res.text}")

        # 断言：系统应该识别攻击并拦截 (返回 400) 或者 至少不让登录成功
        # 如果返回 200 {"success": True}，说明注入成功，系统存在漏洞 -> 测试失败
        # 如果返回 400 或 包含 "error"，说明防御成功 -> 测试通过
        
        is_blocked = res.status_code == 400
        has_error_msg = "error" in res.text.lower()
        
        assert is_blocked or has_error_msg, "严重漏洞：SQL 注入攻击未被拦截！"
        
    except requests.exceptions.ConnectionError:
        pytest.fail("连接失败，请确保 Flask 服务已启动 (flask run)")

if __name__ == "__main__":
    # 允许直接运行脚本
    test_sql_injection_attack()
    print("✅ 安全测试通过：SQL 注入攻击被成功拦截。")