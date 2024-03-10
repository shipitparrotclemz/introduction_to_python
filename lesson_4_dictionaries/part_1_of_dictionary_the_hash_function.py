def hash_str_to_list_index(search_term: str) -> int:
    """
    Challenge: Defining your first re-usable piece of code
    Call these pieces of code a function

    def <function_name>(<inputs_to_function>: <type_of_input>) -> <output_type>:
        <your_implementation_here>

    Takes in a string
    Converts it to an index
    to store that string inside the dictionary

    Number is guaranteed to be from 0 to 1023
    """
    return hash(search_term) % 1024


if __name__ == "__main__":
    my_list: list[str] = [None] * 1024
    wei_xuan: str = "Wei Xuan"
    weixuan_index_in_list: int = hash_str_to_list_index(wei_xuan)
    print(weixuan_index_in_list)

    my_list[weixuan_index_in_list] = wei_xuan
    weixuan_index_in_list: int = hash_str_to_list_index(wei_xuan)
    print(my_list[weixuan_index_in_list])
