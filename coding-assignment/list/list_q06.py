#Remove duplicate elements from a list.
def remove_duplicates(lst):
    return list(set(lst))

# Example
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
