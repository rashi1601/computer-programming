#Check whether a list is sorted in ascending order.
def is_sorted(lst):
    return lst == sorted(lst)

# Example
print(is_sorted([1, 2, 3, 4, 5]))  # Output: True
print(is_sorted([3, 2, 1]))        # Output: False
