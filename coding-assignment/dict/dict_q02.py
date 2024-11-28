#Count the occurrences of each character in a given string using a dictionary.
def char_count(string):
    return {char: string.count(char) for char in string}

# Example
print(char_count("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
