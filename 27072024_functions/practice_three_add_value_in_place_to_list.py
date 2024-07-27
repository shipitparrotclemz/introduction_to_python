# Q: Do all functions need to return something?
# No, we can make it return nothing
# we can give the function an output of None
# None -> means nothing; returns nothing

def add_value_to_list(initial_list: list[str], new_value: str) -> None:
    """
    Add a value to a list, in-place
    - Modifies it directly
    """
    initial_list.append(new_value)
    # no return statement
    # if none is provided, then the python function will return nothing


list_of_macdonalds_visitors: list[str] = []
# line 13, the function returns nothing
# but, it does change something; it adds elson into list_of_macdonalds_visitors
# we edited the list directly
result: None = add_value_to_list(list_of_macdonalds_visitors, "elson")
print(f"result: {result}")
# we expect "elson"
print(list_of_macdonalds_visitors)