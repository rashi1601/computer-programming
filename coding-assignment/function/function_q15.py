#Write a function to find the largest word in a sentence.
def largest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(largest_word("Find the largest word in this sentence"))
# Output: sentence
