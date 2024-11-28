#Sort a list of tuples by the second element.
def sort_by_second_element(lst):
    return sorted(lst, key=lambda x: x[1])

# Example
print(sort_by_second_element([(1, 3), (2, 1), (4, 2)]))  # Output: [(2, 1), (4, 2), (1, 3)]
