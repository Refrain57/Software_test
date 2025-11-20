"""
Unit tests for the palindrome module.
"""
import pytest

from palindrome import is_palindrome

class TestPalindrome:
    """Test cases for is_palindrome function."""

    def test_simple_word(self):
        """Test simple lowercase palindromes."""
        assert is_palindrome("madam") is True
        assert is_palindrome("radar") is True

    def test_case_insensitivity(self):
        """Test that capitalization is ignored."""
        assert is_palindrome("RaceCar") is True
        assert is_palindrome("Level") is True

    def test_complex_sentence(self):
        """Test sentences with spaces and punctuation."""
        assert is_palindrome("A man, a plan, a canal: Panama") is True
        assert is_palindrome("Was it a car or a cat I saw?") is True

    def test_non_palindrome(self):
        """Test strings that are not palindromes."""
        assert is_palindrome("hello") is False
        assert is_palindrome("openai") is False

    def test_empty_string(self):
        """Test that an empty string is considered a palindrome."""
        assert is_palindrome("") is True

    def test_invalid_input_type(self):
        """Test that non-string inputs raise TypeError."""
        with pytest.raises(TypeError):
            is_palindrome(123)
        with pytest.raises(TypeError):
            is_palindrome(None)