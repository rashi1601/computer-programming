#Find the key(s) with the maximum value in a dictionary.
def keys_with_max_value(d):
    max_value = max(d.values())
    return [key for key, value in d.items() if value == max_value]

# Example
d = {'a': 1, 'b': 3, 'c': 3, 'd': 2}
print(keys_with_max_value(d))  # Output: ['b', 'c']
