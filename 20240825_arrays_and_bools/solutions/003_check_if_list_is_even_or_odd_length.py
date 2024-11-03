"""
Create a list with 7 numbers

my_list: list[int] = [1,2,3,4,5,6,7]

If the length of the list is even length, print "List is even length!"

If the length of the list is odd length, print "List is odd length!"
"""

my_list: list[int] = [1, 2, 3, 4, 5, 6, 7]

if len(my_list) % 2 == 0:
    print("List is even length!")
else:
    print("List is odd length!")
