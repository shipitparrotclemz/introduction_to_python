"""
Challenge 1:

Convert wei_xuan: str -> into an int from 0 to 1023

hash(wei_xuan) % length_of_the_list

Reminder:
% -> gives back the remainder of an int after dividing by 1024

569

Why is it 569
Every character represents a number in a mapping table
- We cover this in depth another day

Concept:
- hash() function -> converts a string into an integer.
This integer can be very large / very small
We can't use this as the index right away
The number must be 0 <= X < length_of_list - 1
- % as a hack, to convert an integer within a range of 0 to length_of_list
number % length_of_list -> 0 to length_of_list - 1
"""
length_of_list: int = 1024
my_list: list[str | None] = [None] * length_of_list
wei_xuan: str = "Wei Xuan"
weixuan_index: int = hash(wei_xuan) % length_of_list
print(weixuan_index)
my_list[weixuan_index] = wei_xuan
print(my_list[weixuan_index])
