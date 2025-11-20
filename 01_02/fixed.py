# 修复后的 divide 函数
def divide_fixed(a, b):
    # 修复缺陷1: 增加除数为0的检查
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

# 修复后的 find_max 函数
def find_max_fixed(lst):
    # 修复缺陷2: 处理空列表，并将初始值设为列表第一个元素（或负无穷）
    if not lst:
        return None
    max_val = lst[0]  # 使用第一个元素作为基准，而不是硬编码的 0
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

# 修复后的 get_item 函数
def get_item_fixed(lst, idx):
    # 修复缺陷3: 增加索引范围检查
    if 0 <= idx < len(lst):
        return lst[idx]
    else:
        print(f"Error: Index {idx} out of range.")
        return None