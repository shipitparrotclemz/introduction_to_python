"""
Q: We are using append on a list, to add an item to the back

How would the time taken be like (faster / slower)
if we define a list, and then just add a single list with one item to the back
"""

# my_list: list[str] = ["Item"] * 1000000

"""
first approach:

my_list.append("another item")

second approach:
my_new_list: list[str] = my_list + ["another item"]
"""

"""
Q: What if we have an original list of 1,000,000 items

if i wish to add ten more items, i should use append instead of redefining a new list of 1,000,010 items right?

A: Yes. use append 10 times
- This will save you the need to redefine a new list of 1,000,010 items

Let me prove it to you again

Concept:
"""
from datetime import datetime
from typing import Callable, Any


def timeit(func: Callable[[...], Any]) -> Any:
    """
    This is a magic wand that edits a magic wand
    To print out how long it takes
    """

    def timed_function(*args, **kwargs) -> Any:
        start: datetime = datetime.utcnow()
        result: Any = func(*args, **kwargs)
        end: datetime = datetime.utcnow()
        total_seconds: float = (end - start).total_seconds()
        print(f"{func.__name__} took {total_seconds} seconds")
        return result

    return timed_function


@timeit
def redefine_list_approach(original_list: list[str], item: str) -> list[str]:
    """
    Inefficient approach:

    Given an original_list
    and an item to add

    We "add" the list of items to the back of the original list, by recreating a new list
    """
    # redefines the list
    copy_of_original_list: list[str] = [item for item in original_list]
    new_list: list[str] = copy_of_original_list + [item]
    return new_list


@timeit
def append_list_approach(original_list: list[str], item: str) -> list[str]:
    """
    efficient approach:

    Given an original_list
    and an item to add

    We "add" the list of items to the back of the original list, by using append
    """
    original_list.append(item)
    return original_list


"""
"item" -> x0123 ["item"]

item_to_add -> x0124 [x0123]

"""
item_to_add: str = "item"

"""
[] -> x0124 [ x0200[x0126], x0202[x0127], ... ]
"item" -> x0125 ["item"]
"item" * 1000000 

"item" -> x0126 ["item"] 
"item" -> x0127 ["item"] 
"item" -> x0128 ["item"] 
"item" -> x0129 ["item"] 
....
"""
original_list_one: list[str] = ["item"] * 1000000
# 14,000 microseconds
redefine_list_approach(original_list_one, item_to_add)

original_list_two: list[str] = ["item"] * 1000000
# 43 microseconds to append 1 item
append_list_approach(original_list_two, item_to_add)
