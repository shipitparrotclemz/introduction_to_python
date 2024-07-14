class Nurse:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def clean_shit(self, shit: int) -> int:
        # takes in int as the amount of shit left
        # reduce it by 1
        return shit - 1


nurse: Nurse = Nurse("Clement", 29)
shit_left: int = 100
print(f"shit left before cleaning: {shit_left}")
shit_left = nurse.clean_shit(shit_left)
print(f"shit left after cleaning: {shit_left}")