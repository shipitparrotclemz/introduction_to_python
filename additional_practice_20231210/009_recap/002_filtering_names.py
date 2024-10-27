my_names: list[str] = [
    "Aaron",
    "Clement",
    "Zheng Yang",
    "Eugene",
    "Elson",
    "Gabriel",
    "Wei Xuan",
    "Joyce"
]

# Challenge: Give a list of names, which contains only names with 5 characters
# answer: list[str] = ["Aaron", "Elson", "Joyce"]
answer: list[str] = []
for names in my_names:
    if len(names) == 5:
        answer.append(names)
print(answer)

