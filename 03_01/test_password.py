# test_password.py
import pytest
from password import isValidPassword

# 定义测试数据：(输入, 预期结果, 用例ID/描述)
test_data = [
    # --- 边界值分析 (Boundary Value Analysis) ---
    ("a1b2c",         False, "TC-BVA-01: 长度5 (下边界-1)"),
    ("a1b2c3",        True,  "TC-BVA-02: 长度6 (下边界)"),
    ("a1b2c3d",       True,  "TC-BVA-03: 长度7 (下边界+1)"),
    ("a1b2c3d4e5f",   True,  "TC-BVA-04: 长度11 (上边界-1)"),
    ("a1b2c3d4e5f6",  True,  "TC-BVA-05: 长度12 (上边界)"),
    ("a1b2c3d4e5f6g", False, "TC-BVA-06: 长度13 (上边界+1)"),

    # --- 等价类划分 (Equivalence Class Partitioning) ---
    ("password123",   True,  "TC-ECP-01: 有效输入 (字母+数字)"),
    ("12345678",      False, "TC-ECP-02: 无效 (缺失字母)"),
    ("password",      False, "TC-ECP-03: 无效 (缺失数字)"),
    ("!@#$%^&*",      False, "TC-ECP-04: 无效 (纯符号)"),
    ("pass@123",      True,  "TC-ECP-05: 有效 (字母+数字+符号)"),
    ("",              False, "TC-ECP-06: 无效 (空字符串)")
]

@pytest.mark.parametrize("input_str, expected, case_desc", test_data)
def test_isValidPassword(input_str, expected, case_desc):
    """
    执行密码验证函数的测试用例
    """
    print(f"\nTesting {case_desc} -> Input: '{input_str}'")
    assert isValidPassword(input_str) == expected