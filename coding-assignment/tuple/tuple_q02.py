#Sort a tuple of tuples based on the second element of each tuple.
def sort_by_second(tpl):
    return tuple(sorted(tpl, key=lambda x: x[1]))

# Example
print(sort_by_second(((1, 3), (2, 2), (4, 1))))  # Output: ((4, 1), (2, 2), (1, 3))
