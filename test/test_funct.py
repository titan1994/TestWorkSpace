﻿import builtins
import sys
from pprint import pprint


def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num

    return incrementer


accum = counter()

print(accum())
print(accum())
print(accum())

pprint(dir(builtins))

candy = 5


def get_candy():
    global candy
    candy += 1
    print('У меня {} конфет.'.format(candy))


get_candy()
get_candy()
print(candy)

pprint(sys.modules)

'''
Сравнение nonlocal и атрибутов функции - фишки уровня middle. 
Курим питон в затяг. 
'''


def tester(start):
    def nested(label):
        print(label, nested.state)  # nested – объемлющая область видимости
        nested.state += 1  # Изменит атрибут, а не значение имени nested

    nested.state = start  # Инициализация после создания функции
    return nested


F = tester(0)
F('spam')
F('ham')


def tester2(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


F = tester2(0)
F('spam')
F('ham')
