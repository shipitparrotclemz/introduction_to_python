"""
Your company wants you to do some data transformation on data
"""


# def <name_of_function>(<name_of_input_one>: type_hint, <name_of_input_two>: type_hint) -> <output_type>:
def filter_out_values(input_list: list[str], filter_list: list[str]) -> list[str]:
    filtered_values: list[str] = []
    for value in input_list:
        if value in filter_list:
            continue
        filtered_values.append(value)
    # return a value, of the output type
    return filtered_values


# 27-07-2024
names: list[str] = ["weixuan", "aaron", "clement", "elson"]
names_caught_in_macdonalds: list[str] = ["elson"]

# Filter out the people who have been caught in macdonalds

# Problem Statement
# you have implemented a piece of code
# that solves a problem: filtering out names
# but it seems that we have to copy and paste this everytime
# we want to use this logic
filtered_names: list[str] = filter_out_values(names, names_caught_in_macdonalds)

# 28-07-2024
names: list[str] = ["weixuan", "aaron", "clement", "elson", "gabriel"]
names_caught_in_macdonalds: list[str] = ["elson", "gabriel"]

# Filter out the people who have been caught in macdonalds

filtered_names: list[str] = filter_out_values(names, names_caught_in_macdonalds)
