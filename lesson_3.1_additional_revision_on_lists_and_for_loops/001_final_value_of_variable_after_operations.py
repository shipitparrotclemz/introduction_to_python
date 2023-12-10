"""
Q: Multi-part question

Concepts:
1. Define a list
2. int / str data types
3. == operators to compare two values, returning True or False
4. Using True or False expressions in if-else statements to perform code selectively
5. Iterating a List with a For-loop

(Completed) Step 1: Create a list with strictly these 5 numbers
my_list: list[int] = [1, -1, 1, 1, -1]

Objective:
1. Define a list[int]. It should only contain 1 or -1

[1, -1, 1, 1, -1] -> 0x123

my_list [0x123] -> contains address to list
it is not the list itself
"""
"""
When you create a variable two and assign it to
another variable one

We don't recreate the contents variable one
variable two, will contain the address
to the same list object

This gives us the benefit of not copying
items needlessly

my_list_two [0x123]
"""
# my_list_two: list[int] = my_list
# my_list_two.append(10)

"""
Hypothesis:
- Now that we know variables in python contains addresses
Since my_list_two contains the address to list [1, -1, 1, 1, -1] (0x123)
and my_list contains the address to the same list (0x123)

We expect printing my_list and my_list_two to give

[1, -1, 1, 1, -1, 10]
                  ^
                  we just added this  
"""
# print(my_list)
# print(my_list_two)

"""
Q: In a list, does the list contain 
the actual int object itself?

or do they contain a variable that contains
the address to the actual int object too?

A: They contain variable that contains
the address to the actual int object

the actual int object is stored separately
from the list object
"""

my_list: list[int] = [1, -1, 1, 1, -1]
"""
Step 2: Now that we have defined a list

We will define an int variable representing
the sum of numbers inside my_list

Then, we will use a for-loop to iterate the numbers in my_list
to update the sum

This is a very common pattern for getting the sum of items in a list

Concepts:
- int
- for-loops

Side Concept:
- Tracing 

Q: What is the difference between """""" and # 
- """""" -> this is a multi-line comment
# -> single line comments
comments are pieces of text not considered as instructions
they are used to take notes
yes, we use them alot in production
to communicate with other SWEs on micro-details in code

Concept: high-light code and use command + / on apple to mass comment code
"""
current_sum: int = 0    # 1
for num in my_list: # -1
    current_sum = current_sum + num
    # new concept: you can shorten 88 with +=
    # += it adds the number directly to current_sum
    # current_sum += num
print(current_sum)

"""
Challenge 3: We will now edit challenge 2 to have the following concepts:

- int
- for-loops
(new) - str
(new) - == to compare strings -> gives True / False
(new) - if-else to use the output True / False to do A or B

Define a list containing only ++X, X++, X--, --X

operations: list[str] = ["++X", "X--", "++X", "--X"]

++X / X++ -> increment final_value by 1
--X / x-- -> decrement final_value by 1
"""
final_value: int = 0
operations: list[str] = ["++X", "X--", "++X", "--X"]

for operation in operations:
    if operation == "++X" or operation == "X++":    # str, ==, if-else, True or True -> True
        final_value += 1
    else:
        final_value -= 1

print(final_value)

"""
or , and as boolean operators

or -> only left or right boolean must be true, to be true
-> it will execute expressions from left to right

Optional detail: no need to know this now
expression -> 1 == 1 or 2 == 2
-> since 1 == 1 -> true, and or knows it only needs one of them to be true
-> or wont execute 2 == 2, saving computation
"""
# output: bool = True or False # -> true
# print(output)

"""
and -> both left and right boolean must be true, to be true

Optional detail: 
- for and, it must evaluate all expressions, as it needs all expressions to be true
1 == 1 and 2 == 2
and must evaluate all, even if 1 == 1 is true
"""
# output: bool = True and True
# print(output)

"""
else is the fall-back
if all if expressions above are False
else will execute

Concept:
you can use elif to chain if-else checks
use else as the final chain -> it is always going to execute as a default unless expressions above evaluates to True
"""
# if False:
#     print("clemz is handsome")
# elif False:
#     print("king of taiwan is handsome")
# else:
#     print("weixuan more handsome")