# Practices on Lists

## Challenge 1: Creating a List
- Define a list object named `my_list` containing integers `1`, `2`, `3`, `4`, `5`
- Print `my_list`

```commandline
python3 001_creating_list.py 
[1, 2, 3, 4, 5]
```

## Challenge 2: Accessing Elements in a List
- Define a list object my_list containing integers 10, 20, 30, 40, 50
- Access and print the third element of my_list

```commandline
python3 002_accessing_elements_in_list.py 
30
```

## Challenge 3: Slicing a List
- Define a list object my_list containing integers 1 through 10
- Slice for items from index 2 to index 5 inclusive
- print elements from index 2 to 5 from my_list
- Key concept: the end index is not inclusive; you have to provide index 6 as your input for the end index

```commandline
python3 003_slicing_list.py 
[3, 4, 5, 6]
```

## Challenge 4: Modifying Elements in a List
- Define a list object my_list containing integers 10, 20, 30, 40, 50
- Change the fourth element of my_list to 35
- Print my_list

```commandline
python3 004_modifying_elements_in_list.py 
[10, 20, 30, 35, 50]
```

## Challenge 5: Adding Elements to a List
- Define a list object my_list containing integers 1, 2, 3
- Add 4 and 5 to the end of my_list
- Print my_list

```commandline
python3 005_adding_elements_to_list.py 
[1, 2, 3, 4, 5]
```

## Challenge 6: Removing Elements from a List
- Define a list object my_list containing integers 10, 20, 30, 40, 50
- Remove 30 from my_list
- Print my_list

WARNING: pop() method on list is expensive, and requires a full iteration of the list in the worst case
- The worst case happens when 30 is at the back of the list
- The python interpreter / implementation of pop() needs to iterate from front to back to find 30

We usually don't use it in technical interviews

```commandline
python3 006_removing_elements_from_list.py 
[10, 20, 40, 50]
```

## Challenge 7: List Length
- Define a list object my_list containing integers 5, 10, 15, 20, 25
- Calculate and print the length of my_list

```commandline
python3 007_list_length.py 
5
```

## Challenge 8: Checking Element Existence in a List
- Define a list object my_list containing strings apple, banana, cherry, date
- Check if banana is present in my_list and print the result

```commandline
python3 008_check_element_existence_in_list.py 
True
```

## Challenge 9: Combining Lists
- Define two lists list1 containing integers 1, 2, 3 and list2 containing integers 4, 5, 6
- Combine list1 and list2 into a single list and print the combined list

```commandline
python3 009_combining_lists.py 
[1, 2, 3, 4, 5, 6]
```

## Challenge 10: List Comprehension
- Implement a list comprehension to create a list of squares of numbers from 1 to 5
- Print the list

```commandline
python3 010_list_comprehension.py 
[1, 4, 9, 16, 25]
```