funct = lambda *args: \
    print(args)

funct(13, 2323)


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler)
print(mydoubler(11))


def func(num):
    return num**2


def higher_order_func(fun, num):
    return fun(num)+fun(num)


print(func(4))
print(higher_order_func(func,4))


import math #Подключаем библиотеку math

pi_const = round(math.pi, 2) #округляем pi до второго знака
# после запятой иначе она будет выглядеть
# как 3.141592653589793 а нам это будет неудобно

funct_radius = lambda radius: pi_const*(radius**2)

print(funct_radius(5))
print(funct_radius(10))

asoiaf_books = [
  {'title' : 'Game of Thrones', 'published' : '1996-08-01', 'pages': 694},
  {'title' : 'Clash of Kings', 'published' : '1998-11-16', 'pages': 761},
  {'title' : 'Storm of Swords', 'published' : '2000-08-08', 'pages': 973},
  {'title' : 'Feast for Crows', 'published' : '2005-10-17', 'pages': 753},
  {'title' : 'Dance with Dragons', 'published' : '2011-07-12', 'pages': 1016}
]

asoiaf_books2 = ['1', '2', '3']
for books in sorted(asoiaf_books2):
    print(books)

for book in sorted(asoiaf_books, key=lambda book: book.get('title')):
    print(book)

print('---------------------------')

asoiaf_books.sort(key=lambda book: book.get('pages'))
for book in asoiaf_books:
    print(book)

print('---------------------------')


def get_title(book):
    return book.get('title')


asoiaf_books.sort(key=get_title)
for book in asoiaf_books:
    print(book)

print('--------Копать хоронить-------------------')
a = (lambda x: x+1)(2)

print(a)

