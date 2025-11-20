from locust import HttpUser, task, between
import random
import string

class WebsiteUser(HttpUser):
    # 模拟用户在请求之间的思考时间 (1到3秒)
    # 如果要测试极限吞吐量，可以将此值调低
    wait_time = between(1, 3)

    @task
    def register(self):
        # 生成随机用户名，避免全是 "409 Conflict" 错误
        # 这样我们才能真正测试数据库的"写入"性能，而不是"查询"性能
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        username = f"user_{random_suffix}"
        password = "password123"

        payload = {
            "username": username,
            "password": password
        }

        # 发送 POST 请求
        # catch_response=True 允许我们自定义什么是"成功"或"失败"
        with self.client.post("/register", json=payload, catch_response=True) as response:
            if response.status_code == 201:
                response.success()
            elif response.status_code == 409:
                # 如果随机到了重复用户，视为业务逻辑正常，不算系统错误
                response.success()
            elif response.status_code == 503:
                 # 503 代表数据库锁死，这正是我们想测出来的瓶颈
                response.failure("数据库锁定 (Database Locked)")
            else:
                response.failure(f"未知错误: {response.status_code}")