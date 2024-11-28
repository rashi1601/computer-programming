#Count the number of unique elements in a tuple.
def count_unique(tpl):
    return len(set(tpl))

# Example
print(count_unique((1, 2, 2, 3, 4, 4, 5)))  # Output: 5
