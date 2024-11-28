#Flatten a nested list into a single list.
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]

# Example
print(flatten_list([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]
