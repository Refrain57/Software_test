import requests
import pytest

# 服务地址 (确保 Flask 正在运行)
BASE_URL = "http://127.0.0.1:5000/order"

def test_order_success():
    """测试正常下单流程"""
    payload = {"item": "book", "qty": 2}
    res = requests.post(BASE_URL, json=payload)
    
    assert res.status_code == 200
    data = res.json()
    assert data["success"] == True
    # 初始库存10，买2个，应该剩8个 (假设这是第一个运行的测试)
    # 注意：集成测试中数据状态是持久的，顺序很重要
    assert "剩余库存" in data

def test_order_invalid_item():
    """测试不存在的商品"""
    payload = {"item": "iphone", "qty": 1}
    res = requests.post(BASE_URL, json=payload)
    
    assert res.status_code == 400
    assert res.json()["error"] == "不存在的商品"

def test_order_insufficient_inventory():
    """测试库存不足的情况"""
    # 试图购买超量库存 (比如 100 本)
    payload = {"item": "book", "qty": 100}
    res = requests.post(BASE_URL, json=payload)
    
    assert res.status_code == 400
    assert res.json()["error"] == "库存不足"