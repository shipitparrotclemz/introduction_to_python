# # True or False
# my_bool: bool = True
# print(my_bool)
#
# # Concept: You can use == to check if a value on the left is equal to the right
# # check if a value is == 10
# value: int = 10
# value_is_ten: bool = value == 10
#
# # Challenge 1:
# # Create a value of type float and assign to 10.1
# # Create another variable of type bool, and make it True, if value is equal to 10.1
# # Expected: True
# my_value: float = 10.1
# value_is_ten_point_one: bool = my_value == 10.1
# print(value_is_ten_point_one)
#

bmi_float: float = 30.0
# >= will return True, if bmi_float more or equal to 30.0
# do_operation_on_patient: bool = bmi_float >= 30.0   # Q: True / False?

# Concept 2: <= -> True if the blood_glucose_level is less than or equal to 10.0
# blood_glucose_level: float = 10.0

# Concept 3: == If name is equal to Gabriel, do operation
name: str = "Gabriel"
ph_level: int = 8
do_operation_on_patient: bool = ph_level == 7  # Q: True / False?

# Concept 4: > -> returns true, if

# Concept 5: < ->

# Will the operation be performed?

if do_operation_on_patient:
    print("Perform operation")
else:
    print("Don't perform operation")