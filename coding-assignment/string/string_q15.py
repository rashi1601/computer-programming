#Remove duplicate characters from a string.
def remove_duplicates(s):
    return ''.join(dict.fromkeys(s))

# Example
print(remove_duplicates("hello"))  # Output: "helo"
