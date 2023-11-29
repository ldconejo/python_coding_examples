class PointExample:
    x = 1
    y = 2
    one_list = [1,2,3]

class Person:

    def __init__(self, name="Jane", last_name="Doe"):
        self.name = name
        self.last_name = last_name
        self.one_list = [1,2,3]
        self.ssn = None
        self.age = -99
        slogan = "I might be right or wrong, but not undecided"
        #print(f"A new instance of Person has been created for {self.name} {self.last_name}")
        #print(f"Slogan is {slogan}")

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}"

    def __str__(self) -> str:
        return f"This person's name is {self.name}"

    def introduce(self):
        return f"The name associated to this instance is {self.name} {self.last_name}"
    
    def ask_for_age(self):
        age = input(f"What is {self.name}'s age? ")
        self.age = int(age)

    def increase_age(self):
        # self.age = self.age + 1
        self.age += 1

if __name__ == "__main__":
    instance1 = Person("Luis", "Conejo")
    #print(instance1.name)
    #print(instance1.ssn)
    instance2 = Person()
    #print(instance2.introduce())
    instance2.ask_for_age()
    instance2.increase_age()
    print(f"{instance2.name} is now {instance2.age}")
    instance1.increase_age()
