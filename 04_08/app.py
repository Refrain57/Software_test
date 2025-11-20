import sqlite3
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# 数据库初始化
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # 创建一个简单的用户表
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  username TEXT UNIQUE, 
                  password TEXT)''')
    conn.commit()
    conn.close()

# 初始化数据库
init_db()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "缺少用户名或密码"}), 400

    try:
        # --- 模拟业务逻辑瓶颈 ---
        # 1. 模拟 CPU 密集型计算 (例如密码哈希过程的简化)
        # 这会导致在高并发下 CPU 使用率飙升
        sum([i**2 for i in range(5000)]) 
        
        # 2. 模拟 I/O 瓶颈 (SQLite 文件锁)
        # SQLite 在写入时会锁定整个文件，并发写入时会产生大量阻塞
        conn = sqlite3.connect('users.db', timeout=5) 
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        
        return jsonify({"msg": "注册成功", "username": username}), 201

    except sqlite3.IntegrityError:
        return jsonify({"msg": "用户名已存在"}), 409
    except sqlite3.OperationalError:
        # 当并发过高，SQLite 锁超时时会抛出此错误
        return jsonify({"msg": "数据库繁忙 (Locked)"}), 503
    except Exception as e:
        return jsonify({"msg": str(e)}), 500

if __name__ == '__main__':
    # 启动 Flask 开发服务器
    # 注意：Flask 默认是单线程/单进程模式 (在某些版本可能是多线程但受 GIL 限制)
    # 这也是系统测试中的一个重要瓶颈点
    print("服务器启动在 http://localhost:5000")
    app.run(debug=False, port=5000)