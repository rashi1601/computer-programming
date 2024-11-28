#Split a list into two parts.
def split_list(lst, n):
    return lst[:n], lst[n:]

# Example
print(split_list([1, 2, 3, 4, 5], 3))  # Output: ([1, 2, 3], [4, 5])
