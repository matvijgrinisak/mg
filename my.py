from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @abstractmethod
    def make_sound(self):
        pass


    def get_info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"



class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"



class Cat(Animal):
    def make_sound(self):
        return "Няв-няв!"



class Parrot(Animal):
    def make_sound(self):
        return "Привіт!"



dog = Dog("Шерлок", 5)
cat = Cat("Мурка", 3)
parrot = Parrot("Кеша", 2)


animals = [dog, cat, parrot]
for animal in animals:
    print(animal.get_info())
    print(animal.make_sound())
    print()

