from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # 模拟用户在执行任务之间等待 1 到 3 秒
    wait_time = between(1, 3)

    @task
    def order_book(self):
        """
        定义一个任务：模拟用户发送下单请求
        """
        # 发送 POST 请求到 /order 接口
        self.client.post("/order", json={"item": "book", "qty": 1})
