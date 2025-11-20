import requests
import multiprocessing
import time
import pytest
from flask import Flask, request, jsonify

# --- 1. 定义微服务应用 (模拟 app/checkout_service.py) ---
app = Flask(__name__)

@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()
    items = data.get("items", [])
    if not items: 
        return jsonify({"error": "empty cart"}), 400
    total = sum(i["price"] * i["quantity"] for i in items)
    return jsonify({"total": total, "status": "ok"}), 200

# --- 2. 定义服务启动函数 ---
def run_server():
    # 禁用调试器输出以保持测试报告整洁
    # Windows 下多进程启动 Flask 建议明确指定 host
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)

# --- 3. 测试用例实现 ---
def test_checkout_total():
    """
    测试目标：验证单商品计算逻辑是否正确
    输入：价格 20，数量 3
    预期：总价 60，状态码 200
    """
    # 步骤 1: 在子进程中启动 Flask 服务
    p = multiprocessing.Process(target=run_server)
    p.daemon = True # 设置为守护进程
    p.start()
    
    # 等待服务启动
    time.sleep(1) 
    
    try:
        # 步骤 2: 准备测试数据
        # 【修复点】这里必须是纯字符串，不能包含 Markdown 格式
        url = "http://127.0.0.1:5000/checkout"
        data = {"items": [{"price": 20, "quantity": 3}]}
        
        # 步骤 3: 发送请求
        res = requests.post(url, json=data)
        
        # 步骤 4: 断言验证
        # 验证 HTTP 状态码
        assert res.status_code == 200, f"Expected 200, got {res.status_code}"
        
        # 验证业务逻辑返回值的正确性
        response_json = res.json()
        assert response_json["total"] == 60, f"Expected total 60, got {response_json.get('total')}"
        assert response_json["status"] == "ok"
        
    finally:
        # 步骤 5: 清理环境，终止服务进程
        p.terminate()
        p.join()