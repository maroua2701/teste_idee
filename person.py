class Person:
    def __init__(self, name, age):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
    def majeur(self):
        if self.age >= 18:
            return True
        else:
            return False

    def greet(self):
        if self.majeur():
                return f"Hello, my name is {self.name} and I am {self.age} years old. I am an adult."
        else:
             return f"Hello, my name is {self.name} and I am {self.age} years old, I am not an adult."
    def get_perso(self):
        return self.name, self.age