class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("An animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

animal.speak()
dog.speak()
cat.speak()
