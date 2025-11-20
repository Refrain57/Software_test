import pytest
from library_system import LibrarySystem

# 使用 fixture 初始化测试环境，确保每个测试用例都有一个新的系统实例
@pytest.fixture
def lib():
    return LibrarySystem()

# --- 测试用例 ---

# 用例 1: 正常借阅流程
def test_borrow_success(lib):
    """测试正常借书：用户存在，书存在且有库存"""
    initial_stock = lib.books["Python编程从入门到实践"]
    result = lib.borrow_book("Alice", "Python编程从入门到实践")
    
    # 断言：返回值为 True，且库存减少了 1
    assert result is True
    assert lib.books["Python编程从入门到实践"] == initial_stock - 1

# 用例 2: 异常情况 - 用户不存在
def test_user_not_found(lib):
    """测试借书失败：用户不存在，应抛出异常"""
    with pytest.raises(ValueError) as excinfo:
        lib.borrow_book("NonExistentUser", "Python编程从入门到实践")
    
    # 断言：异常信息包含特定提示
    assert "用户 'NonExistentUser' 不存在" in str(excinfo.value)

# 用例 3: 异常情况 - 图书不存在
def test_book_not_found(lib):
    """测试借书失败：图书未收录，应抛出异常"""
    with pytest.raises(ValueError) as excinfo:
        lib.borrow_book("Bob", "哈利波特")
    
    # 断言：异常信息包含特定提示
    assert "图书 '哈利波特' 未收录" in str(excinfo.value)

# 用例 4: 异常情况 - 库存为 0
def test_stock_empty(lib):
    """测试借书失败：库存为0，应抛出异常"""
    with pytest.raises(ValueError) as excinfo:
        lib.borrow_book("Charlie", "被借光的书")
    
    # 断言：异常信息包含特定提示
    assert "目前无库存" in str(excinfo.value)
    # 确保库存没有变成负数
    assert lib.books["被借光的书"] == 0

# 用例 5: 边界测试 - 借走最后一本书
def test_borrow_last_book(lib):
    """测试边界：借走库存仅剩1本的书，库存应变为0"""
    initial_stock = lib.books["绝版孤本"] # 初始为 1
    
    lib.borrow_book("Bob", "绝版孤本")
    
    # 断言：库存变为 0
    assert lib.books["绝版孤本"] == 0
    
    # 再次尝试借阅同一本书，应该失败
    with pytest.raises(ValueError):
        lib.borrow_book("Alice", "绝版孤本")