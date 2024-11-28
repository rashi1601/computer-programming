#Group elements of a list by their frequency using a dictionary.
def group_by_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

# Example
print(group_by_frequency([1, 2, 2, 3, 3, 3, 4]))  # Output: {1: 1, 2: 2, 3: 3, 4: 1}
