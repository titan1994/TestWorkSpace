"""
Декораторы
"""


def class_all_decoration(function_decorator):
    """
    Универсальный декоратор класса

    Args:
        function_decorator: Любой декоратор

    """

    def track_exception(cls):
        # Все колл-атрибуты (по факту функции)
        callable_attributes = {k: v for k, v in cls.__dict__.items() if callable(v)}

        # Декорирование всех функций
        for name, func in callable_attributes.items():
            decorated = function_decorator(func)
            setattr(cls, name, decorated)
        return cls

    return track_exception


# def counter(func):
#     """
#     Р”РµРєРѕСЂР°С‚РѕСЂ, СЃС‡РёС‚Р°СЋС‰РёР№ Рё РІС‹РІРѕРґСЏС‰РёР№ РєРѕР»РёС‡РµСЃС‚РІРѕ РІС‹Р·РѕРІРѕРІ
#     РґРµРєРѕСЂРёСЂСѓРµРјРѕР№ С„СѓРЅРєС†РёРё.
#     """
#
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         res = func(*args, **kwargs)
#         print("{0} Р±С‹Р»Р° РІС‹Р·РІР°РЅР°: {1}x".format(func.__name__, wrapper.count))
#         return res
#
#     wrapper.count = 0
#     return wrapper
#
#
# @class_all_decoration(counter)
# class A:
#     lisp = 10
#
#     def f1(self, lie=20):
#         print('1 ', lie)
#
#     def f2(self, lie=20):
#         print('2', lie)
#
#
# a = A()
# a.f1()
# a.f2()


def singleton(cls):
    """
    Простой синглтон

    Args:
        cls:
    """

    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton

#
# @singleton
# class TheOne:
#     pass


# print('СЃС‚Р°СЂС‚')
# first_one = TheOne()
# second_one = TheOne()
# print(id(first_one))
# print(id(second_one))
# print('РєРѕРЅРµС†')
