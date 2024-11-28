#Check if one string is a substring of another.
def is_substring(s1, s2):
    return s1 in s2

# Example
print(is_substring("world", "hello world"))  # Output: True
print(is_substring("python", "hello world"))  # Output: False
