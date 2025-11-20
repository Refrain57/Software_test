import sys

# ==========================================
# Part 1: 原始程序片段 (包含 3 个缺陷)
# ==========================================
def divide(a, b):
    return a / b   # 缺陷1: 未检查除数为0

def find_max(lst):
    max_val = 0    # 缺陷2: 初始值为0，全负数列表会出错
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

def get_item(lst, idx):
    return lst[idx]  # 缺陷3: 未检查索引越界

# ==========================================
# Part 2: 测试用例执行器 (执行 6 个用例)
# ==========================================
def run_test_case(test_id, func, args, expected, description):
    print(f"--- 执行 {test_id}: {description} ---")
    print(f"输入: {args}")
    print(f"预期结果: {expected}")
    
    try:
        # 根据参数数量调用不同函数
        if len(args) == 2:
            result = func(*args)
        else:
            result = func(args[0])
            
        print(f"实际结果: {result}")
        
        if result == expected:
            print("状态: ✅ PASS (通过)")
        else:
            print("状态: ❌ FAIL (失败 - 结果不符)")
            
    except Exception as e:
        print(f"实际结果: 程序崩溃/异常")
        print(f"异常信息: {type(e).__name__}: {e}")
        print("状态: ❌ FAIL (失败 - 异常崩溃)")
    print("\n")

if __name__ == "__main__":
    print("====== 开始执行测试用例 ======\n")

    # --- 针对 divide 的测试 ---
    # 用例 1: 正常除法
    run_test_case("TC-01", divide, (10, 2), 5.0, "验证正常除法")
    # 用例 2: 除数为0 (触发缺陷 1)
    run_test_case("TC-02", divide, (5, 0), None, "验证除数为0的情况")

    # --- 针对 find_max 的测试 ---
    # 用例 3: 正数列表
    run_test_case("TC-03", find_max, ([1, 5, 3],), 5, "验证正数列表最大值")
    # 用例 4: 全负数列表 (触发缺陷 2)
    run_test_case("TC-04", find_max, ([-10, -5, -3],), -3, "验证全负数列表最大值")

    # --- 针对 get_item 的测试 ---
    # 用例 5: 正常索引
    run_test_case("TC-05", get_item, ([10, 20, 30], 1), 20, "验证正常索引访问")
    # 用例 6: 索引越界 (触发缺陷 3)
    run_test_case("TC-06", get_item, ([10, 20, 30], 5), None, "验证索引越界情况")

    print("====== 测试结束 ======")