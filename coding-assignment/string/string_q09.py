#Count the frequency of each character in a string.
from collections import Counter

def char_frequency(s):
    return Counter(s)

# Example
print(char_frequency("hello"))  # Output: Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})
