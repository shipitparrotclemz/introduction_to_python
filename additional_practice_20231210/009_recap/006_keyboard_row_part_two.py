"""
Given a keyboard

QWERTYUIOP
ASDFGHJKL
ZXCVBNM

And a list of words

["DAD", "ALASKA", "GAS", "AARON", "ELSON"]

Return the row for each word (I.E, the row for the 1st character)

ASDFGHJKL

Hint:
- To get the first character of a word: str

first_char: str = word[0]

- To check if a character is in the 2nd row

second_row: str = "ASDFGHJKL"
if first_char in second_row:
    # do something
"""

words: list[str] = ["DAD", "ALASKA", "GAS", "AARON", "ELSON"]
# answer: list[str] = ["DAD", "ALASKA", "GAS"]  # all on 2nd row

first_row: set[str] = set("QWERTYUIOP")
second_row: set[str] = set("ASDFGHJKL")
third_row: set[str] = set("ZXCVBNM")

answer: list[str] = []
for word in words:  # word = "DAD"
    first_char: str = word[0].upper()  # "D"
    if first_char in first_row:  # "D" in "QWERTYUIOP" -> False
        row = first_row
    elif first_char in second_row:  # "D" in "ASDFGHJKL" -> True
        row = second_row  # row = "ASDFGHJKL"
    else:
        row = third_row
    # Step 2: Check all characters in the string, if they belong to the row
    # row = second_row
    # check if "AD" in row "ASDFGHJKL"

    is_valid_bool: bool = True
    for curr_char in word:
        if curr_char not in row:
            is_valid_bool = False
            break
    if is_valid_bool:
        answer.append(word)
print(answer)


print(answer)
