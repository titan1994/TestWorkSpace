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
    """
    Args:
        func:
    """
    @functools.wraps(func)
    def wrapper(self, lie=40):
        lie -= 10
        return func(self, lie)

    return wrapper


def counter(func):
    """Р”РµРєРѕСЂР°С‚РѕСЂ, СЃС‡РёС‚Р°СЋС‰РёР№ Рё РІС‹РІРѕРґСЏС‰РёР№
    РєРѕР»РёС‡РµСЃС‚РІРѕ РІС‹Р·РѕРІРѕРІ РґРµРєРѕСЂРёСЂСѓРµРјРѕР№ С„СѓРЅРєС†РёРё.

    Args:
        func:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} Р±С‹Р»Р° РІС‹Р·РІР°РЅР°: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper


def class_all_decoration(function_decorator):
    """РЎРѕР±СЂР°Р» РєРѕРјР±Рѕ РёР· РёРЅС‚РµСЂРЅРµС‚Р°. РљРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ
    РґРµРєРѕСЂР°С‚РѕСЂРѕРІ, РєРѕС‚РѕСЂС‹Р№ СЃС‚СЂРѕРёС‚ РєРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ
    РґРµРєРѕСЂР°С‚РѕСЂРѕРІ РєР»Р°СЃСЃРѕРІ РћРґРЅРѕ РІ РґСЂСѓРіРѕРµ Рё РІ
    РёС‚РѕРіРµ - Сѓ РЅР°СЃ РїР°СЂР°РјРµС‚СЂРёР·РѕРІР°РЅРЅС‹Р№
    СѓРЅРёРІРµСЂСЃР°Р»СЊРЅС‹Р№ РєРѕРЅСЃС‚СЂСѓРєС‚РѕСЂ РґРµРєРѕСЂР°С†РёР№

    Args:
        function_decorator: СЌС‚Рѕ Р·Р°СЂР°РЅРµРµ РѕРїСЂРµРґРµР»РµРЅРЅС‹Р№
            РґРµРєРѕСЂР°С‚РѕСЂ
    """

    def track_exception(cls):
        # РџРѕР»СѓС‡Р°РµРј РІСЃС‘ С‡С‚Рѕ РјРѕР¶РЅРѕ РґРµРєРѕСЂРёСЂРѕРІР°С‚СЊ
        callable_attributes = {k: v for k, v in cls.__dict__.items() if callable(v)}

        # Р’СЃС‚Р°РІР»СЏРµРј РІСЃРµ Р°С‚СЂРёР±СѓС‚С‹ РєСѓРґР° РјРѕР¶РµРј
        for name, func in callable_attributes.items():
            decorated = function_decorator(func)
            setattr(cls, name, decorated)
        return cls

    return track_exception


@class_all_decoration(method_friendly_decorator)
class A:
    lisp = 10

    def f1(self, lie=20):
        """
        Args:
            lie:
        """
        print('1 ', lie)

    def f2(self, lie=20):
        """
        Args:
            lie:
        """
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
        """
        Args:
            func:
        """
        print('> РљР»Р°СЃСЃ Decorator РјРµС‚РѕРґ __init__')
        self.func = func
        print(func.__name__)

    def __call__(self):
        print('> РїРµСЂРµРґ РІС‹Р·РѕРІРѕРј РєР»Р°СЃСЃР°...', self.func.__name__)
        self.func()
        print('> РїРѕСЃР»Рµ РІС‹Р·РѕРІР° РєР»Р°СЃСЃР°')


@Decorator
def wrapped():
    print('С„СѓРЅРєС†РёСЏ wrapped')


print('>> СЃС‚Р°СЂС‚')
wrapped()
print('>> РєРѕРЅРµС†')


class DecoratorArgs:
    def __init__(self, name):
        """
        Args:
            name:
        """
        print('> Р”РµРєРѕСЂР°С‚РѕСЂ СЃ Р°СЂРіСѓРјРµРЅС‚Р°РјРё __init__:', name)
        self.name = name

    def __call__(self, func):
        """
        Args:
            func:
        """
        def wrapper(a, b):
            print('>>> РґРѕ РѕР±РµСЂРЅСѓС‚РѕР№ С„СѓРЅРєС†РёРё')
            func(a, b)
            print('>>> РїРѕСЃР»Рµ РѕР±РµСЂРЅСѓС‚РѕР№ С„СѓРЅРєС†РёРё')

        return wrapper


@DecoratorArgs("teste")
def add(a, b):
    """
    Args:
        a:
        b:
    """
    print('С„СѓРЅРєС†РёСЏ add:', a, b)


print('>> СЃС‚Р°СЂС‚')
add(10, 20)
print('>> РєРѕРЅРµС†')

print('++++' * 80)

"""
РћР±СЂР°С‚РЅС‹Р№ РІС‹Р·РѕРІ РєРѕР»Р»Р±Р°Рє РјР°С‚СЊ РµРіРѕ
"""

app = {}


def callback(route):
    """
    Args:
        route:
    """
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


print('> СЃС‚Р°СЂС‚')
route = app.get('/')
if route:
    resp = route()
    print('РѕС‚РІРµС‚:', resp)

print('> РєРѕРЅРµС†')

print(app)

"""
РџСЂРѕРІРµСЂРєР° РґРѕСЃС‚СѓРїРѕРІ 
"""

print('++++' * 80)

user_permissions = ["user", "admin"]


def check_permission(permission):
    """
    Args:
        permission:
    """
    def wrapper_permission(func):
        def wrapped_check():
            if permission not in user_permissions:
                raise ValueError("РќРµРґРѕСЃС‚Р°С‚РѕС‡РЅРѕ РїСЂР°РІ")
            return func()

        return wrapped_check

    return wrapper_permission


@check_permission("user")
def check_value():
    return "Р·РЅР°С‡РµРЅРёРµ"


@check_permission("admin")
def do_something():
    return "С‚РѕР»СЊРєРѕ Р°РґРјРёРЅ"


print('СЃС‚Р°СЂС‚ РїСЂРѕРіСЂР°РјРјС‹')
print(check_value())
print(do_something())
print('РєРѕРЅРµС† РїСЂРѕРіСЂР°РјРјС‹')

print('++++' * 80)

"""
РЎРёРЅРіРµР»СЊС‚РѕРЅ
"""


def singleton(cls):
    """РљР»Р°СЃСЃ Singleton (РѕРґРёРЅ СЌРєР·РµРјРїР»СЏСЂ)

    Args:
        cls:
    """

    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


print('СЃС‚Р°СЂС‚')
first_one = TheOne()
second_one = TheOne()
print(id(first_one))
print(id(second_one))
print('РєРѕРЅРµС†')

print('++++' * 80)

"""
Р›РѕРіРµСЂ РѕС€РёР±РѕРє
"""


def error_handler(func):
    """
    Args:
        func:
    """
    def wrapper(*args, **kwargs):
        ret = 0
        try:
            ret = func(*args, **kwargs)
        except Exception:
            print('>> РћС€РёР±РєР° РІ С„СѓРЅРєС†РёРё', func.__name__)
        return ret

    return wrapper


@error_handler
def div(a, b):
    """
    Args:
        a:
        b:
    """
    return a / b


print('СЃС‚Р°СЂС‚')
print(div(10, 2))
print(div(10, 0))
print('РєРѕРЅРµС†')


x, y = 50, 25
small = x if x < y else y
print(small)
