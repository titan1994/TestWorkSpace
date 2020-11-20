
class Car:

    @staticmethod
    def get_class_details():
        print("Это класс Car")

    @staticmethod
    def get_squares(a, b):
        return a*a, b*b

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Car {}'.format(self.name)


Car.get_class_details()

a, b = Car.get_squares(2, 3)
print(a, b)

bmw = Car('BMW')

print(bmw)


class sampleclass:
    count = 0  # атрибут класса

    def increase(self):
        sampleclass.count += 1


# Вызов увеличения () для объекта

s1 = sampleclass()
s1.increase()
print(s1.count)

s2 = sampleclass()
s2.increase()

print(s1.count)

print(sampleclass.count)


# создание класса Vehicle
class Vehicle:
    def print_details(self):
        print("Это родительский метод из класса Vehicle")


# создание класса, который наследует Vehicle
class Car(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Car")


# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):
    def print_details(self):
        print("Это дочерний метод из класса Cycle")



car_a = Vehicle()
car_a.print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()