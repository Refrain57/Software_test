import pytest
from text_utils import truncate_string

class TestTruncateString:
    
    # 用例 1: 测试正常未超长的情况 (覆盖分支 B)
    def test_no_truncation_needed(self):
        input_text = "Hello"
        limit = 10
        result = truncate_string(input_text, max_length=limit)
        
        # 断言：结果应与输入完全一致
        assert result == "Hello"
        assert len(result) <= limit

    # 用例 2: 测试超长需要截断的情况 (覆盖分支 C)
    def test_truncation_with_default_suffix(self):
        input_text = "This is a very long sentence."
        limit = 10
        # 预期结果: "This is..." (7个字符 + 3个字符后缀 = 10)
        result = truncate_string(input_text, max_length=limit)
        
        # 断言：长度符合限制，且以默认后缀结尾
        assert result == "This is..."
        assert len(result) == limit
        assert result.endswith("...")

    # 用例 3: 测试非法输入类型 (覆盖分支 A)
    def test_invalid_input_type(self):
        invalid_input = 123456  # 传入整数而非字符串
        
        # 断言：必须抛出 TypeError 异常
        with pytest.raises(TypeError) as exc_info:
            truncate_string(invalid_input)
        
        # 验证异常信息是否准确
        assert str(exc_info.value) == "Input content must be a string"