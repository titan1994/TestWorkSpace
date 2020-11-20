def numbers_range(n):
    for i in range(n):
        yield i


a = numbers_range(4)
print(type(a))
for b in a:
    print(b)


def subgenerator():
    yield 'World'


def generator():
    yield 'Hello'
    yield from subgenerator()  # Запрашиваем значение из субгенератора
    yield '!'


for i in generator():
    print(i)


class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration


s_iter2 = SimpleIterator(5)
for i in s_iter2:
    print(i)


def fibonacci(xterms):
    # первые два условия
    x1 = 0
    x2 = 1
    count = 0

    print('febonachi')

    if xterms <= 0:
        print("Укажите целое число больше 0")
    elif xterms == 1:
        print("Последовательность Фибоначчи до", xterms, ":")
        print(x1)
    else:
        while count < xterms:
            print(' что продолжает елд')
            xth = x1 + x2
            x1 = x2
            x2 = xth
            count += 1
            yield xth


print('-' * 200)
fib = fibonacci(5)
print('-' * 200)

for i in fib:
    print(i)

print('-' * 200)

kvs = ['23', '32']
print(list(((lambda _: '-o')((yield x)) for x in kvs))[::-1])

print(list(x for x in range(22)))

L = [x for x in range(22)]
print(list(map(lambda x: x ** 2, L)))

print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)
L = [Alex, Amanda, David]

L.sort(key=lambda x: x.age)
print([item.name for item in L])


def my_yeld_test(num):
    akt = 10 - num
    yield akt


for i in range(10):
    a = my_yeld_test(i)
    for l in a:
        print(l)

gen_expr = (var ** (1 / 2) for var in range(10))

print(gen_expr)


def AP(a1, d, size):
    count = 1
    while count <= size:
        yield a1
        a1 += d
        count += 1


for ele in AP(1, 2, 10):
    print(ele)

# def find_prime():
#     num = 1
#     while True:
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 yield num
#         num += 1
#
# for ele in find_prime():
#     print(ele)

print('+' * 90)


def find_prime():
    num = 1
    while num < 100:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    yield num
        num += 1


def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num


a_pipeline = find_odd_prime(find_prime())

for a_ele in a_pipeline:
    print(a_ele)

import sys

g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print(sys.getsizeof(g))

l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print(sys.getsizeof(l))


data = [i for i in range(0, 10) if i % 2 == 0]
print(data)

data = [(i , j) for i in range(0, 3) for j in range(0, 3)]
print(data)

data = [(lambda i: i*i)(i) for i in range(0, 10)]
print(data)

data = [i*i for i in range(0, 10)]
print(data)

name_install = '777'
name_pack = '22'

name_install = name_install if len(name_install) > 0 else name_pack
print(name_install)