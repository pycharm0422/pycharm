class Pets:

    dogs = []
    def __init__(self, dogs):
        self.dogs = dogs

class Dog(Pets):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old :"

class Tyler(Dog):
    def run(self,speed):
        return f"{self.name} runs with {speed}"

class Demon(Dog):
    def run(self, speed):
        return f"{self.name} runs with the speed of {speed}"

my_pets = [Dog("charlie", 3), Tyler("tyler", 6), Demon("zeb", 5)]

print(f"I have {len(my_pets)} dogs:")

my_dogs = Pets(my_pets)

for dog in my_dogs.dogs:
    print()

