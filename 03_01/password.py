# password.py

def isValidPassword(s: str) -> bool:
    """
    验证密码是否符合规范：
    1. 长度 6-12 位
    2. 必须包含数字
    3. 必须包含字母
    """
    # 规则1：长度检查 (6 <= len <= 12)
    if not (6 <= len(s) <= 12):
        return False
    
    # 规则2：包含数字
    has_digit = any(char.isdigit() for char in s)
    
    # 规则3：包含字母
    has_alpha = any(char.isalpha() for char in s)
    
    # 必须同时满足所有条件
    return has_digit and has_alpha