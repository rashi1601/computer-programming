#Find the second largest element in a list.
def second_largest(lst):
    lst = list(set(lst))  # Remove duplicates
    lst.sort()
    return lst[-2]

# Example
print(second_largest([3, 5, 7, 2, 8]))  # Output: 7
