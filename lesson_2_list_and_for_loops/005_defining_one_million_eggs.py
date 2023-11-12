# eggs: list[str] = ["Egg 1", "Egg 2", ... "Egg 99"]
eggs: list[str] = []

for i in range(1000000):    # 0 to 99
    egg: str = "Egg " + str(i)  # E.G "Egg 1"
    eggs.append(egg)

print(eggs)