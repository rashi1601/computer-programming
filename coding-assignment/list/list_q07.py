#Find the common elements in two lists.
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Example
print(intersection([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]
