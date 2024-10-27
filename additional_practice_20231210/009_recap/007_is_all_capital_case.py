word: str = "ELsON"

"""
Return a bool if word is all upper case

is_upper_case: bool = False
"""
# answer: list[str] = []
is_upper_case: bool = True
for curr_char in word:
    if not curr_char.isupper():
        is_upper_case = False
        break
    # if is_upper_case:
    #     answer.append(word)
print(is_upper_case)