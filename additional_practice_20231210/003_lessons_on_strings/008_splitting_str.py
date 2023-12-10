"""
## Challenge 8: Splitting a String
- Define a string object "Welcome to the Python world" and assign its value to a variable named my_str
- Split my_str into a list of words and assign it to a variable named words_list
- Print words_list
"""
my_str: str = "Welcome to the Python world"
words_list: list[str] = my_str.split(" ")
print(words_list)