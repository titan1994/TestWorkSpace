
"""
РЎРѕР±РёСЂР°РµРј РїРѕС‚РёС…РѕРЅСЊРєСѓ РєСЂСѓС‚С‹Рµ РїР»СЋС€РєРё РїРѕ РґРµРєРѕСЂР°С‚РѕСЂР°Рј
"""

import functools


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


# print('СЃС‚Р°СЂС‚')
# first_one = TheOne()
# second_one = TheOne()
# print(id(first_one))
# print(id(second_one))
# print('РєРѕРЅРµС†')
