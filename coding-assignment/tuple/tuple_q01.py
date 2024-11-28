#Write a program to find the indices of all occurrences of a specific element in a tuple.
def find_indices(tpl, element):
    return [index for index, value in enumerate(tpl) if value == element]

# Example
print(find_indices((1, 2, 3, 2, 4, 2), 2))  # Output: [1, 3, 5]
