
class Car:

    @staticmethod
    def get_class_details():
        print("Р­С‚Рѕ РєР»Р°СЃСЃ Car")

    @staticmethod
    def get_squares(a, b):
        """
        Args:
            a:
            b:
        """
        return a*a, b*b

    def __init__(self, name):
        """
        Args:
            name:
        """
        self.name = name

    def __str__(self):
        return 'Car {}'.format(self.name)


Car.get_class_details()

a, b = Car.get_squares(2, 3)
print(a, b)

bmw = Car('BMW')

print(bmw)


class sampleclass:
    count = 0  # Р°С‚СЂРёР±СѓС‚ РєР»Р°СЃСЃР°

    def increase(self):
        sampleclass.count += 1


# Р’С‹Р·РѕРІ СѓРІРµР»РёС‡РµРЅРёСЏ () РґР»СЏ РѕР±СЉРµРєС‚Р°

s1 = sampleclass()
s1.increase()
print(s1.count)

s2 = sampleclass()
s2.increase()

print(s1.count)

print(sampleclass.count)


# СЃРѕР·РґР°РЅРёРµ РєР»Р°СЃСЃР° Vehicle
class Vehicle:
    def print_details(self):
        print("Р­С‚Рѕ СЂРѕРґРёС‚РµР»СЊСЃРєРёР№ РјРµС‚РѕРґ РёР· РєР»Р°СЃСЃР° Vehicle")


# СЃРѕР·РґР°РЅРёРµ РєР»Р°СЃСЃР°, РєРѕС‚РѕСЂС‹Р№ РЅР°СЃР»РµРґСѓРµС‚ Vehicle
class Car(Vehicle):
    def print_details(self):
        print("Р­С‚Рѕ РґРѕС‡РµСЂРЅРёР№ РјРµС‚РѕРґ РёР· РєР»Р°СЃСЃР° Car")


# СЃРѕР·РґР°РЅРёРµ РєР»Р°СЃСЃР° Cycle, РєРѕС‚РѕСЂС‹Р№ РЅР°СЃР»РµРґСѓРµС‚ Vehicle
class Cycle(Vehicle):
    def print_details(self):
        print("Р­С‚Рѕ РґРѕС‡РµСЂРЅРёР№ РјРµС‚РѕРґ РёР· РєР»Р°СЃСЃР° Cycle")



car_a = Vehicle()
car_a.print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()
