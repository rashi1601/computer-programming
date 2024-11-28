#Find the first non-repeated character in a string.
from collections import Counter

def first_non_repeated(s):
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

# Example
print(first_non_repeated("swiss"))  # Output: "w"
