#Flatten a nested tuple into a single tuple.
def flatten_tuple(tpl):
    result = []
    for item in tpl:
        if isinstance(item, tuple):
            result.extend(flatten_tuple(item))
        else:
            result.append(item)
    return tuple(result)

# Example
print(flatten_tuple((1, (2, 3), (4, (5, 6)))))  # Output: (1, 2, 3, 4, 5, 6)
