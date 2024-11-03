"""
Leetcode Easy

Concepts:
- String
- Using a for loop to iterate characters in a String
- Using == to check if a string is a space " " -> returns True or False
- Using number of spaces to infer the number of words (1 space between words = 2 words)
- Using for-loop + int variable to keep track of the sum of something (what we encountered in final value of variable after operations)
"""

"""
Step 1:
Define a sentence: str
- A sentence contains words, separated by a single space
- No apostrophes, no commas

Concept: defining a str
"""
# 10 words
sentence: str = "vivian doesn't look at looks she only cares about personality"

"""
Step 2: Split the sentence into a list[str] (containing words)
words: list[str] = ["vivian", "doesn't", "look", "at", "looks", "she", "only", "cares", "about", "personality"]

Concepts:
- For loop to iterate characters in sentence
- Using == operator to compare each character (str) == " " empty space
    - useful to let us know if we just finished reading a word
- Define a list[str] to store words in a sentence

1. Know when it is the end of a word in a sentence -> space character == " "
    - for loop
    - str
    - == operator to check str
2. once you have a word, you have to append it to the list
    - when to append -> end of a word (if-else)
    - define a list
    - append to a list
"""
# keep track of words
# keep track of current word
# spoiler: this is not optimal, i will explain later
# hint: strings are immutable in python; we have to recreate a new string everytime we edit it
# we will look at using list[str] to store each character later
# we want to clear the current word after we put the word into words
# so the next word will not contain the previous word
# we are only putting words into words, when we encounter a space
# the last word doesn't have a space at the back
# we will miss out the last word
words: list[str] = (
    []
)  # ["vivian", "doesn't", "look", "at", "looks", "she", "only", "cares", about"]
current_word: str = ""  # "personality"
sentence: str = "vivian doesn't look at looks she only cares about personality"
#                                                                            ^
for char in sentence:
    # we are in the middle of a current word
    # add each character into current_word
    if char != " ":
        current_word = current_word + char
        # current_word += char
    else:
        # empty " " - we reached the end of a word
        # add the current word into words: list[str]
        words.append(current_word)
        # reset current_words to empty string, so next word doesn't contain previous word
        current_word = ""
words.append(current_word)
# not necessary anymore; you aren't using current_word from this point anyway
# this is redundant
# current_word = ""
print(words)
