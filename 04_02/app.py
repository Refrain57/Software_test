from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库中的库存
inventory = {"book": 10}

@app.route("/order", methods=["POST"])
def order():
    """
    处理订单请求的接口
    期望 JSON: {"item": "商品名", "qty": 数量}
    """
    data = request.get_json()
    
    # 获取参数
    item = data.get("item")
    qty = data.get("qty", 1)  # 默认为 1
    
    # 1. 校验商品是否存在
    if item not in inventory:
        return jsonify({"error": "不存在的商品"}), 400
    
    # 2. 校验库存是否充足
    if inventory[item] < qty:
        return jsonify({"error": "库存不足"}), 400
    
    # 3. 扣减库存 (模拟支付成功后的操作)
    inventory[item] -= qty
    
    return jsonify({
        "success": True, 
        "message": "下单成功",
        "剩余库存": inventory[item]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)