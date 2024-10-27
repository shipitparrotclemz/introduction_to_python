list_of_numbers: list[int] = [i for i in range(1, 101)]

# Challenge:
# For this list of 1,2,3,...99,100
# filter out only numbers which are less than 10
# answer: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_of_numbers)
answer: list[int] = []
for number in list_of_numbers:
    if number < 10:
        answer.append(number)
print(answer)