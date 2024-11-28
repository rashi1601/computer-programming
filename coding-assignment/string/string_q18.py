#Check if a string is alphanumeric.
def is_alphanumeric(s):
    return s.isalnum()

# Example
print(is_alphanumeric("hello123"))  # Output: True
print(is_alphanumeric("hello 123"))  # Output: False
