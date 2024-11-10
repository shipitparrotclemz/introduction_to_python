my_str: str = "We are studying in starbucks"
#                 ^
expected_result: list[str] = ["We", "are", "studying", "in", "starbucks"]

words: list[str] = []

# this tells us the start of the previous word
start_of_word_index: int = 0

for index in range(len(my_str)):
    curr_char: str = my_str[index]
    if curr_char == " ":
        curr_word: str = my_str[start_of_word_index:index]  # "We"
        words.append(curr_word)
        start_of_word_index = index + 1
# the last word not appended yet
curr_word: str = my_str[start_of_word_index:]
words.append(curr_word)

print(words)

