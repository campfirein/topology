def reverse_string(s):
    """Reverse a given string."""
    return s[::-1]

def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]

def count_vowels(s):
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)