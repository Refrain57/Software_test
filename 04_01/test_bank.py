import pytest
from bank import transfer

def test_transfer_normal():
    """测试正常转账情况"""
    a = {"balance": 100}
    b = {"balance": 50}
    
    # 执行转账
    result = transfer(a, b, 30)
    
    # 验证返回值和余额变化
    assert result == True
    assert a["balance"] == 70
    assert b["balance"] == 80

def test_transfer_negative():
    """测试负数金额抛出异常"""
    a, b = {"balance": 100}, {"balance": 50}
    
    # 验证是否抛出 ValueError，并且错误信息匹配
    with pytest.raises(ValueError, match="转账金额必须为正数"):
        transfer(a, b, -10)

def test_transfer_insufficient_balance():
    """测试余额不足抛出异常"""
    a, b = {"balance": 20}, {"balance": 50}
    
    # 验证余额不足逻辑
    with pytest.raises(ValueError, match="余额不足"):
        transfer(a, b, 50)