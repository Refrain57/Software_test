from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/checkout", methods=["POST"])
def checkout():
    """
    处理结账请求的端点
    期望的 JSON 格式: {"items": [{"price": 10, "quantity": 2}, ...]}
    """
    data = request.get_json()
    # 获取 items 列表，如果不存在则默认为空列表
    items = data.get("items", [])
    
    # 边界条件处理：如果购物车为空，返回 400 错误
    if not items:
        return jsonify({"error": "empty cart"}), 400
    
    # 核心业务逻辑：计算所有商品的总价 (单价 * 数量)
    total = sum(i["price"] * i["quantity"] for i in items)
    
    # 返回计算结果和 200 状态码
    return jsonify({"total": total, "status": "ok"}), 200

if __name__ == "__main__":
    # 启动 Flask 开发服务器，默认运行在 5000 端口
    app.run(port=5000, debug=True)