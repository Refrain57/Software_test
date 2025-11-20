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
@app.route("/login", methods=["GET"])
def login_page():
    """
    返回 HTML 登录页面
    包含 id="username" 等元素供 Selenium 查找
    """
    return """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>系统登录</title>
    </head>
    <body>
        <h1>用户登录</h1>
        <form>
            <!-- Selenium 测试脚本会查找 id="username" -->
            <label for="username">用户名:</label>
            <input type="text" id="username" name="username" placeholder="请输入用户名">
            <br><br>
            
            <!-- Selenium 测试脚本会查找 id="password" (可选) -->
            <label for="password">密码:</label>
            <input type="password" id="password" name="password">
            <br><br>
            
            <button type="button" id="btn-login">登录</button>
        </form>
    </body>
    </html>
    """
if __name__ == '__main__':
    # 启动服务，监听 5000 端口
    print("启动 Flask 服务...")
    print("-> 接口地址: http://127.0.0.1:5000/order")
    print("-> 页面地址: http://127.0.0.1:5000/login")
    app.run(debug=True, port=5000)