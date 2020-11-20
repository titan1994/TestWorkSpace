
"""
Собираем потихоньку крутые плюшки по декораторам
"""

import functools


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


# def counter(func):
#     """
#     Декоратор, считающий и выводящий количество вызовов
#     декорируемой функции.
#     """
#
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         res = func(*args, **kwargs)
#         print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
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
    """Класс Singleton (один экземпляр)"""

    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


# print('старт')
# first_one = TheOne()
# second_one = TheOne()
# print(id(first_one))
# print(id(second_one))
# print('конец')
