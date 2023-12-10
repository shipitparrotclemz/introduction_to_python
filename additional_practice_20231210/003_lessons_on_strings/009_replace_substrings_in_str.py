"""
## Challenge 9: Replacing Substrings in a String
- Define a string object "I like cats, but I also like dogs" and assign its value to a variable named my_str
- Replace all occurrences of "cats" with "birds" in my_str and assign it to a variable named new_str
- Print new_str
"""
my_str: str = "I like cats, but I also like dogs"
new_str: str = my_str.replace("cats", "birds")
print(new_str)