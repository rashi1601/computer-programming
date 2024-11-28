#Reverse the order of words in a string.
def reverse_words(s):
    return ' '.join(s.split()[::-1])

# Example
print(reverse_words("hello world"))  # Output: "world hello"
