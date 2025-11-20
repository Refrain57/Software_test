"""
Palindrome Checker Module.

This module provides functionality to verify if a given string is a palindrome.
It is designed to demonstrate unit testing, code coverage, and linting.
"""

def is_palindrome(text: str) -> bool:
    """
    Determine if the given text is a palindrome.

    The check ignores case sensitivity and non-alphanumeric characters
    (such as spaces, punctuation, and symbols).

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the text is a palindrome, False otherwise.

    Raises:
        TypeError: If the input argument is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    # Use list comprehension to keep only alphanumeric chars and convert to lower
    clean_chars = [char.lower() for char in text if char.isalnum()]

    # Compare the list of characters with its reverse
    return clean_chars == clean_chars[::-1]