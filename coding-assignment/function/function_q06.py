#Write a function to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 3, 2, 4, 4]))  # Output: [1, 2, 3, 4]
