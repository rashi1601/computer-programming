#Replace all occurrences of a specific element in a tuple with a new value.
def replace_element(tpl, old, new):
    return tuple(new if x == old else x for x in tpl)

# Example
print(replace_element((1, 2, 3, 2, 4), 2, 5))  # Output: (1, 5, 3, 5, 4)
