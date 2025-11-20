# 这是一个被测试的简单函数：加法
def add(x, y):
    return x + y

# 这是一个测试用例：验证 1+2 是否等于 3
def test_add():
    assert add(1, 2) == 3