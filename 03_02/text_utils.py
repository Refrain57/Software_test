def truncate_string(content: str, max_length: int = 10, suffix: str = "...") -> str:
    """
    将字符串截断到指定长度。
    如果截断发生，'max_length' 包含了后缀的长度。
    """
    # 逻辑分支 A: 类型保护
    if not isinstance(content, str):
        raise TypeError("Input content must be a string")

    # 逻辑分支 B: 长度在范围内，直接返回
    if len(content) <= max_length:
        return content

    # 逻辑分支 C: 长度超出，进行截断处理
    # 确保给后缀留出空间
    if len(suffix) >= max_length:
        return suffix[:max_length]
    
    cut_length = max_length - len(suffix)
    return content[:cut_length] + suffix