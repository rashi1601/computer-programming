#Find the index of the first occurrence of an element in a list.
def find_index(lst, x):
    return lst.index(x) if x in lst else -1

# Example
print(find_index([1, 2, 3, 4], 3))  # Output: 2
