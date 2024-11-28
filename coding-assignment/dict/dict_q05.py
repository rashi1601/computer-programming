#Write a program to invert a dictionary (swap keys and values).
def invert_dict(d):
    return {value: key for key, value in d.items()}

# Example
print(invert_dict({'a': 1, 'b': 2, 'c': 3}))  # Output: {1: 'a', 2: 'b', 3: 'c'}
