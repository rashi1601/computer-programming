#Count the number of digits in a string.
def count_digits(s):
    return sum(1 for char in s if char.isdigit())

# Example
print(count_digits("hello123"))  # Output: 3
