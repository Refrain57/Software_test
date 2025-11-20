from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_page_content():
    print("正在初始化 Chrome 驱动...")
    
    # --- 核心修改：使用 ChromeDriverManager 自动安装驱动 ---
    try:
        # 自动下载并设置驱动路径
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        print(f"\n====== 驱动初始化失败 ======")
        print(f"错误信息: {e}")
        print("建议：如果自动下载失败，请手动下载 chromedriver.exe 并放到 Python 目录下。")
        return

    try:
        # 1. 访问登录页面 (确保 Flask 服务已启动)
        url = "http://127.0.0.1:5000/login"
        driver.get(url)
        time.sleep(1)  # 等待渲染
        
        # 2. 验证页面标题
        assert "系统登录" in driver.title
        
        # 3. 验证关键元素
        # 查找 ID 为 username 的输入框
        username_input = driver.find_element(By.ID, "username")
        assert username_input is not None
        
        print("✅ UI 测试通过！")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        raise e
        
    finally:
        # 4. 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    test_login_page_content()