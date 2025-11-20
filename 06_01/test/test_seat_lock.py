import sys
import os
import time
import pytest

# 路径修复：确保能导入 app 模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.seat_lock import SeatLockSystem

def test_lock_and_expire():
    """
    测试用例 1：
    1. 锁定座位成功
    2. 手动修改时间模拟过期
    3. 验证座位状态变为未锁定
    """
    s = SeatLockSystem()
    
    # 1. 首次锁定应当成功
    assert s.lock("A1", "user1") is True
    
    # 2. 模拟时间流逝（手动将过期时间设置为过去的时间）
    # 这里的 -1 表示过期时间是当前时间的 1 秒前，即已过期
    s.locked_seats["A1"]["expire"] = time.time() - 1
    
    # 3. 验证应该显示为未锁定
    assert s.is_locked("A1") is False

def test_relock_after_expire():
    """
    测试用例 2：
    1. 锁定座位
    2. 模拟过期
    3. 另一个用户尝试锁定同一座位（应该成功）
    4. 验证座位被重新锁定
    """
    s = SeatLockSystem()
    
    # 1. user1 锁定
    s.lock("A1", "user1")
    
    # 2. 模拟过期
    s.locked_seats["A1"]["expire"] = time.time() - 1
    
    # 3. user2 尝试锁定 (因为已过期，所以应该允许锁定)
    result = s.lock("A1", "user2")
    assert result is True
    
    # 4. 验证当前确实被锁定了
    assert s.is_locked("A1") is True
    
    # 额外验证：确保当前锁定的用户是 user2
    assert s.locked_seats["A1"]["user"] == "user2"