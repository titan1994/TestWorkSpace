"""
Декорирование функций и методов
"""


def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie -= 10
        return method_to_decorate(self, lie)

    return wrapper


class Lucy:
    def __init__(self):
        self.age = 30

    @method_friendly_decorator
    def say_age(self, lie):
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))


lucy = Lucy()
lucy.say_age(30)

'''
Если упороться - то можно задекоировать переменными аргументами
Кароче - это атомная боеголовка
'''


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # Данная "обёртка" принимает любые аргументы
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print(args)
        print(kwargs)
        function_to_decorate(*args, **kwargs)

    print("------Кто безумец? ---- Какой безумец----Я?---- Кто это я---- Это не я ---- Это ты")
    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")


function_with_no_argument()


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)


@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
    print("Любят ли {}, {} и {} утконосов? {}".format(a, b, c, platypus))


function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")


class Mary(object):
    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3):
        # Теперь мы можем указать значение по умолчанию
        print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))


m = Mary()
m.sayYourAge()

"""
Мы накурены, буханы и ум=пороты, но нма мало. А давайте создадим конструктор декораторов
"""

print('---------------------------------')


def decorator_maker():
    print(
        "ГЕНЕРАТОР ДЕОКРАТОРОВ Я создаю декораторы! Я буду вызван только раз: когда ты попросишь меня создать декоратор.")

    def my_decorator(func):
        print("ДКОРАТОР Я! Я буду вызван только раз: в момент декорирования функции.")

        def wrapped():
            print("Я - обёртка вокруг декорируемой функции.\n"
                  "Я буду вызвана каждый раз, когда ты вызываешь декорируемую функцию.\n"
                  "Я возвращаю результат работы декорируемой функции.")
            return func()

        print("Я возвращаю обёрнутую функцию.")
        print("-------------------------------")
        return wrapped

    print("Я возвращаю декоратор.")
    print("-------------------------------")
    return my_decorator


def dec_funct():
    print('!!!не трогай меня ёпть!!!')


new_decorator = decorator_maker()
dec_funct = new_decorator(dec_funct)

dec_funct()

'''
impossible
'''

print('=' * 33)


@decorator_maker()
def next_ddd():
    print('only the best coder like this')


next_ddd()

"""
Шли третьи сутки - а дурь всё не кончалаась
Шобы функции не сошли с ума в нутри декоратора надо сделать стоковый декоратор
"""
import functools

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print("-"*40)
    print("ГЕНЕРАТОР Я создаю декораторы! И я получил следующие аргументы:",
          decorator_arg1, decorator_arg2)

    def my_decorator(func):
        print("Я - декоратор. И ты всё же смог передать мне эти аргументы:",
              decorator_arg1, decorator_arg2)

        # Не перепутайте аргументы декораторов с аргументами функций!
        @functools.wraps(func)
        def wrapped(function_arg1, function_arg2):
            print("Я - обёртка вокруг декорируемой функции.\n"
                  "И я имею доступ ко всем аргументам\n"
                  "\t- и декоратора: {0} {1}\n"
                  "\t- и функции: {2} {3}\n"
                  "Теперь я могу передать нужные аргументы дальше"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments("Леонард", "Шелдон")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
          " {1}".format(function_arg1, function_arg2))


decorated_function_with_arguments("2", "роберт")

print(decorated_function_with_arguments.__name__)


"""

"""


"""
Декоратор, выводящий время, которое заняло
выполнение декорируемой функции.
"""
import time


def benchmark(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = time.process_time()
        res = func(*args, **kwargs)
        print(func.__name__, time.process_time() - t)
        return res

    return wrapper


def logging(func):
    """
    Декоратор, логирующий работу кода.
    (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res

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


@benchmark
@logging
@counter
def reverse_string(string):
    return ''.join(reversed(string))


print(reverse_string("А роза упала на лапу Азора"))
