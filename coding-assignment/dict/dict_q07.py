#Write a program to find the common keys in two dictionaries.
def common_keys(dict1, dict2):
    return set(dict1.keys()) & set(dict2.keys())

# Example
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
print(common_keys(dict1, dict2))  # Output: {'b', 'c'}
