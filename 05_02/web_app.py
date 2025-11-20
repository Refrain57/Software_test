class LoginService:
    """
    模拟 Web 应用的登录服务后端逻辑
    """
    def __init__(self):
        # 模拟数据库中的用户信息
        self.users_db = {
            "student": "Pass123",
            "teacher": "Teach@2024",
            "admin": "Admin#888"
        }

    def login(self, username, password):
        """
        登录函数
        :param username: 用户名
        :param password: 密码
        :return: dict (包含状态码和消息)
        """
        if not username or not password:
            return {"code": 400, "message": "用户名或密码不能为空"}

        if username not in self.users_db:
            return {"code": 404, "message": "用户不存在"}

        stored_password = self.users_db[username]

        # === [BUG 预埋区域] ===
        # 缺陷说明：为了方便调试，开发人员留了一个后门，或者写错了逻辑
        # 只要密码全部小写匹配，或者直接等于 '万能密码' 就能通过
        # 正确逻辑应该是：if password == stored_password:
        
        if password.lower() == stored_password.lower():  # 严重缺陷：忽略了密码大小写
            return {"code": 200, "message": "登录成功"}
        # ======================

        return {"code": 401, "message": "密码错误"}

# 简单的调试入口
if __name__ == "__main__":
    service = LoginService()
    print(service.login("student", "Pass123"))