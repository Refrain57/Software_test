from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库中的库存
# 注意：Flask 每次重启，库存都会重置为 10
inventory = {"book": 10}

# --- 功能 1：订单接口 (供 Postman, Pytest, Locust 使用) ---
@app.route("/order", methods=["POST"])
def order():
    """
    处理订单请求的接口
    期望 JSON: {"item": "book", "qty": 1}
    """
    # 获取请求数据，silent=True 防止空数据报错
    data = request.get_json(silent=True) or {}
    
    item = data.get("item")
    qty = data.get("qty", 1)  # 默认购买数量为 1
    
    # 1. 校验商品是否存在
    if item not in inventory:
        return jsonify({"error": "不存在的商品"}), 400
    
    # 2. 校验库存是否充足
    if inventory[item] < qty:
        return jsonify({"error": "库存不足"}), 400
    
    # 3. 扣减库存
    inventory[item] -= qty
    
    return jsonify({
        "success": True, 
        "message": "下单成功",
        "剩余库存": inventory[item]
    })

# --- 功能 2 & 3：登录页面 (GET) 与 登录验证 (POST) ---
@app.route("/login", methods=["GET", "POST"])
def login():
    """
    GET: 返回 HTML 登录页面 (供 Selenium UI 测试使用)
    POST: 处理登录请求 (供 安全测试/SQL注入测试 使用)
    """
    # --- 处理 API 登录请求 (POST) ---
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        username = data.get("username", "")
        password = data.get("password", "")

        # [安全防御逻辑]：简单的 WAF (Web Application Firewall) 模拟
        # 如果输入包含常见的 SQL 注入特征字符，则拦截
        dangerous_chars = ["'", "--", " OR ", " UNION ", ";", " 1=1 "]
        if any(char in username.upper() for char in dangerous_chars):
            print(f"⚠️ 警告：检测到 SQL 注入尝试! Payload: {username}")
            return jsonify({"error": "非法字符：检测到潜在的 SQL 注入攻击"}), 400

        # 简单的模拟认证
        if username == "admin" and password == "123456":
            return jsonify({"success": True, "message": "登录成功"})
        else:
            return jsonify({"error": "用户名或密码错误"}), 401

    # --- 返回 HTML 页面 (GET) ---
    return """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>系统登录</title>
        <style>
            body { font-family: sans-serif; padding: 20px; }
            .login-box { border: 1px solid #ccc; padding: 20px; width: 300px; }
            input { margin-bottom: 10px; width: 100%; box-sizing: border-box; }
        </style>
    </head>
    <body>
        <h1>用户登录</h1>
        <div class="login-box">
            <form>
                <!-- Selenium 测试脚本会查找 id="username" -->
                <label for="username">用户名:</label>
                <input type="text" id="username" name="username" placeholder="请输入用户名">
                
                <!-- Selenium 测试脚本会查找 id="password" -->
                <label for="password">密码:</label>
                <input type="password" id="password" name="password">
                
                <button type="button" id="btn-login">登录</button>
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    # 启动服务，监听 5000 端口
    print("启动 Flask 服务...")
    print("-> 订单接口: http://127.0.0.1:5000/order (POST)")
    print("-> 登录页面: http://127.0.0.1:5000/login (GET)")
    print("-> 登录接口: http://127.0.0.1:5000/login (POST)")
    app.run(debug=True, port=5000)