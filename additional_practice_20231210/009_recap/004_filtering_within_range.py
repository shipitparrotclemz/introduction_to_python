numbers: list[int] = [i for i in range(1, 201)]     # 1 to 200

# Filter out 50 to 60
# answer: list[int] = [50,51,52,53,54,55,56,57,58,59,60]
# Hint: use <= and >=
# if 50 <= num <= 60
answer: list[int] = []
for number in numbers:
    if 50 <= number <= 60:
        answer.append(number)
print(answer)