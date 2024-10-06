# Practices on Dictionaries

## Challenge 1: Creating a Dictionary
- Define a dictionary named my_dict containing keys 'one', 'two', 'three', 'four', 'five' with corresponding values 1, 2, 3, 4, 5
- Print my_dict

```commandline
python3 001_creating_dictionary.py 
{
    'one': 1, 
    'two': 2, 
    'three': 3, 
    'four': 4, 
    'five': 5
}
```

## Challenge 2: Accessing Elements in a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Access and print the value associated with the 'age' key in my_dict

```commandline
python3 002_accessing_elements_in_dictionary.py 
25
```

## Challenge 3: Modifying Elements in a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Change the value of the 'city' key in my_dict to 'San Francisco'
- Print my_dict

```commandline
python3 003_modifying_elements_in_dictionary.py
{'name': 'Alice', 'age': 25, 'city': 'San Francisco'}
```

## Challenge 4: Adding Elements to a Dictionary
- Define an empty dictionary my_dict
- Add a key 'name' with the value 'Bob' and a key 'age' with the value 30 to my_dict
- Print my_dict

```commandline
python3 004_adding_elements_to_dictionary.py 
{'name': 'Bob', 'age': 30}
```

## Challenge 5: Removing Elements from a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Remove the key-value pair 'age': 25 from my_dict
- Print my_dict

```commandline
python3 005_removing_elements_from_dictionary.py 
{'name': 'Alice', 'city': 'New York'}
```

## Challenge 6: Dictionary Length
- Define a dictionary my_dict containing keys 'a', 'b', 'c', 'd' with corresponding values 1, 2, 3, 4
- Calculate and print the length of my_dict

```commandline
python3 006_dictionary_length.py 
4
```

## Challenge 7: Checking Key Existence in a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Check if the key 'age' is present in my_dict and print the result

```commandline
python3 007_check_key_existence_in_dictionary.py 
True
```

## Challenge 8: Accessing Keys and Values in a Dictionary
- Define a dictionary my_dict containing keys 'name', 'age', 'city' with corresponding values 'Alice', 25, 'New York'
- Print all the keys and values present in my_dict

```commandline
python3 008_accessing_keys_and_values_in_dictionary.py 
Keys: ['name', 'age', 'city']
Values: ['Alice', 25, 'New York']
```

## Challenge 9: Merging Dictionaries
- Define two dictionaries dict1 containing keys 'a', 'b' with values 1, 2 and dict2 containing keys 'c', 'd' with values 3, 4
- Merge dict2 into dict1 and print the updated dict1

```commandline
python3 009_merging_dictionaries.py 
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

## Challenge 10: Dictionary Comprehension
- Implement a dictionary comprehension to create a dictionary of squares of numbers from 1 to 5
- Print the dictionary

```commandline
python3 010_dictionary_comprehension.py 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```