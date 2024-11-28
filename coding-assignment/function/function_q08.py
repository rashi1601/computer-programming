#Write a function to check if a value exists in a list.
def value_exists(lst, value):
    return value in lst

print(value_exists([1, 2, 3, 4], 3))  # Output: True
print(value_exists([1, 2, 3, 4], 5))  # Output: False
