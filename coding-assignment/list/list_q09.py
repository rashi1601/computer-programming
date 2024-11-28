#Rotate a list by a given number of positions.
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

# Example
print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [3, 4, 5, 1, 2]
