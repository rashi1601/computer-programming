#Write a function to count the occurrences of a specific element in a list.
def count_occurrences(lst, elem):
    return lst.count(elem)

print(count_occurrences([1, 2, 3, 2, 2, 4], 2))  # Output: 3
