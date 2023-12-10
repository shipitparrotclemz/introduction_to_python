# Practices on `str`

## Challenge 1: Defining a `str`
- Define a string object (`"Hello"`) and assign its value to a variable named `my_str`
- Print it

### Challenge 1: Expected Answer

```commandline
python3 001_defining_a_str.py 
Hello
```

## Challenge 2: Concatenating two strings
- Define a first string object "Hello," and assign its value to a variable named first_str
- Define a second string object " world!" and assign its value to a variable named second_str
- Define a third string object as the concatenation of first_str and second_str using the + operator
- Assign its value to a variable named concatenated_str
- Print it

```commandline
python3 002_concatenating_two_strs.py 
Hello, world!
```

## Challenge 3: Finding the length of a string
- Define a string object "Python is awesome!" and assign its value to a variable named my_str
- Define an integer object to store the length of my_str using the len() function
- Print the length

```commandline
python3 003_length_of_str.py 
18
```

## Challenge 4: Accessing characters in a string
- Define a string object "Hello" and assign its value to a variable named my_str
- Access and print the first character of my_str

```commandline
python3 004_accessing_chars_in_str.py 
H
```

## Challenge 5: Counting occurrences of a character in a string
- Define a string object "Hello, how are you?" and assign its value to a variable named my_str
- Define a character o to count its occurrences in my_str
- Define an integer object to store the count of occurrences of o using the count() method
- Print the count

WARNING: We usually don't use this in technical interviews.
- It is expensive, and requires a full scan of the string in it's implementation
- To be specific, we call it having a worse case time complexity of O(N)
- Where N is the length of the string
- And the worst case time complexity represents how the implementation of `count`'s time taken to run scale with N

```commandline
python3 005_count_char_occurrences.py
3
```

## Challenge 6: Finding a substring in a string
- Define a string object "Python is powerful!" and assign its value to a variable named my_str
- Define a substring "power" to check its presence in my_str
- Define a boolean object to store whether the substring exists in my_str using the in operator
- Print the result

```commandline
python3 006_find_substring_in_str.py
True
```

## Challenge 7: Changing Case in a String
- Define a string object "HeLLo, HoW ArE YoU?" and assign its value to a variable named my_str
- Convert my_str to lowercase and assign it to a variable named lowercase_str
- Convert my_str to uppercase and assign it to a variable named uppercase_str
- Print both lowercase_str and uppercase_str

```commandline
python3 007_change_case_in_str.py 
hello, how are you?
HELLO, HOW ARE YOU?
```

## Challenge 8: Splitting a String
- Define a string object "Welcome to the Python world" and assign its value to a variable named my_str
- Split my_str into a list of words and assign it to a variable named words_list
- Print words_list

```commandline
python3 008_splitting_str.py 
['Welcome', 'to', 'the', 'Python', 'world']
```

## Challenge 9: Replacing Substrings in a String
- Define a string object "I like cats, but I also like dogs" and assign its value to a variable named my_str
- Replace all occurrences of "cats" with "birds" in my_str and assign it to a variable named new_str
- Print new_str

```commandline
python3 009_replace_substrings_in_str.py 
I like birds, but I also like dogs
```

## Challenge 10: Checking Start and End of a String
- Define a string object "Python is amazing" and assign its value to a variable named my_str
- Check if my_str starts with "Python" and assign the result to a boolean variable named starts_with_python
- Check if my_str ends with "amazing" and assign the result to a boolean variable named ends_with_amazing
- Print both starts_with_python and ends_with_amazing

```commandline
python3 010_check_start_end_str.py 
True
True
```