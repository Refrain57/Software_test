import pytest
from web_app import LoginService

class TestWebLogin:
    """
    Web 登录功能自动化测试套件
    """

    def setup_method(self):
        """每个测试用例执行前的初始化"""
        self.service = LoginService()

    # --- 1. 成功场景 ---
    def test_login_success(self):
        """测试用例 01: 输入正确的用户名和密码，登录成功"""
        result = self.service.login("student", "Pass123")
        assert result["code"] == 200
        assert result["message"] == "登录成功"

    # --- 2. 失败场景 ---
    def test_login_wrong_password(self):
        """测试用例 02: 输入错误的密码，登录失败"""
        result = self.service.login("student", "WrongPass")
        assert result["code"] == 401
        assert result["message"] == "密码错误"

    def test_login_user_not_found(self):
        """测试用例 03: 输入不存在的用户名，登录失败"""
        result = self.service.login("ghost_user", "123456")
        assert result["code"] == 404
        assert result["message"] == "用户不存在"

    def test_login_empty_input(self):
        """测试用例 04: 用户名或密码为空"""
        result = self.service.login("", "Pass123")
        assert result["code"] == 400
        result_none = self.service.login(None, None)
        assert result_none["code"] == 400

    # --- 3. 安全性/边界测试 (旨在发现 Bug) ---
    def test_password_case_sensitivity(self):
        """
        测试用例 05: 密码大小写敏感性测试
        预期结果：密码 'pass123' 应该无法登录 'student' (正确密码是 'Pass123')
        实际情况：如果有 Bug，这里可能会通过，或者我们需要断言它失败
        """
        # 我们预期这是失败的（即 code 应该返回 401）
        result = self.service.login("student", "pass123") 
        
        # 如果代码逻辑正确，这里应该断言 code == 401
        # 但由于我们知道代码里有 bug，这个测试在运行时可能会 fail (因为代码返回了 200)
        # 这正是自动化测试发现缺陷的过程
        assert result["code"] == 401, "严重安全缺陷：系统未区分密码大小写！"

if __name__ == "__main__":
    pytest.main(["-v", "test_login.py"])