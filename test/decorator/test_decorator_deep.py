import functools


class A(object):
    @classmethod
    def foo(cls):
        print(cls.__name__)

    @staticmethod
    def bar():
        print('I have no use for the instance or class')


a = A()

a.foo()
a.bar()

A.foo()
A.bar()


def method_friendly_decorator(func):
    @functools.wraps(func)
    def wrapper(self, lie=40):
        lie -= 10
        return func(self, lie)

    return wrapper


def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


def class_all_decoration(function_decorator):
    """
    Собрал комбо из интернета. Конструктор декораторов, который строит конструктор декораторов классов
    Одно в другое и в итоге - у нас параметризованный универсальный конструктор декораций

    :param function_decorator: это заранее определенный декоратор
    :return:
    """

    def track_exception(cls):
        # Получаем всё что можно декорировать
        callable_attributes = {k: v for k, v in cls.__dict__.items() if callable(v)}

        # Вставляем все атрибуты куда можем
        for name, func in callable_attributes.items():
            decorated = function_decorator(func)
            setattr(cls, name, decorated)
        return cls

    return track_exception


@class_all_decoration(method_friendly_decorator)
class A:
    lisp = 10

    def f1(self, lie=20):
        print('1 ', lie)

    def f2(self, lie=20):
        print('2', lie)


aa = A()
aa.f1()
aa.f1()
aa.f1()
aa.f2()

aa.lisp = 10

print('-' * 400)


class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func
        print(func.__name__)

    def __call__(self):
        print('> перед вызовом класса...', self.func.__name__)
        self.func()
        print('> после вызова класса')


@Decorator
def wrapped():
    print('функция wrapped')


print('>> старт')
wrapped()
print('>> конец')


class DecoratorArgs:
    def __init__(self, name):
        print('> Декоратор с аргументами __init__:', name)
        self.name = name

    def __call__(self, func):
        def wrapper(a, b):
            print('>>> до обернутой функции')
            func(a, b)
            print('>>> после обернутой функции')

        return wrapper


@DecoratorArgs("teste")
def add(a, b):
    print('функция add:', a, b)


print('>> старт')
add(10, 20)
print('>> конец')

print('++++' * 80)

"""
Обратный вызов коллбак мать его
"""

app = {}


def callback(route):
    def wrapper(func):
        app[route] = func
        print('wrap')

        def wrapped():
            print('ret')
            ret = func()
            return ret

        return wrapped

    return wrapper


@callback('/')
def index():
    print('index')
    return 'OK'


print('> старт')
route = app.get('/')
if route:
    resp = route()
    print('ответ:', resp)

print('> конец')

print(app)

"""
Проверка доступов 
"""

print('++++' * 80)

user_permissions = ["user", "admin"]


def check_permission(permission):
    def wrapper_permission(func):
        def wrapped_check():
            if permission not in user_permissions:
                raise ValueError("Недостаточно прав")
            return func()

        return wrapped_check

    return wrapper_permission


@check_permission("user")
def check_value():
    return "значение"


@check_permission("admin")
def do_something():
    return "только админ"


print('старт программы')
print(check_value())
print(do_something())
print('конец программы')

print('++++' * 80)

"""
Сингельтон
"""


def singleton(cls):
    '''Класс Singleton (один экземпляр)'''

    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


print('старт')
first_one = TheOne()
second_one = TheOne()
print(id(first_one))
print(id(second_one))
print('конец')

print('++++' * 80)

"""
Логер ошибок
"""


def error_handler(func):
    def wrapper(*args, **kwargs):
        ret = 0
        try:
            ret = func(*args, **kwargs)
        except Exception:
            print('>> Ошибка в функции', func.__name__)
        return ret

    return wrapper


@error_handler
def div(a, b):
    return a / b


print('старт')
print(div(10, 2))
print(div(10, 0))
print('конец')


x, y = 50, 25
small = x if x < y else y
print(small)