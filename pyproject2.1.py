# 1. Length of longest word in the list
'''Complete the function that takes one argument, 
a list of words, and returns the length of the
longest word in the list'''

def longest_word_length(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

words_list = ["simple","is","better","than","complex"]
max_length = longest_word_length(words_list)
print("The longest word length is: ", max_length)        