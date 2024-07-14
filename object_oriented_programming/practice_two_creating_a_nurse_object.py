class Nurse:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

nurse: Nurse = Nurse("Clement", 29)
print(nurse.name)
print(nurse.age)