#Write a program to create a dictionary by combining two lists: one for keys and one for values.
def create_dict(keys, values):
    return dict(zip(keys, values))

# Example
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(create_dict(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3}
