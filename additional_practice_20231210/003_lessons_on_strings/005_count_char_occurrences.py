"""
## Challenge 5: Counting occurrences of a character in a string
- Define a string object "Hello, how are you?" and assign its value to a variable named my_str
- Define a character o to count its occurrences in my_str
- Define an integer object to store the count of occurrences of o using the count() method
- Print the count
"""

my_str: str = "Hello, how are you?"
char_o: str = "o"
count_of_o_in_my_str: int = my_str.count(char_o)
print(count_of_o_in_my_str)
