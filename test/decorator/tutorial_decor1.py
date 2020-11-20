class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func
        print('Фукнция которую мы оборачиваем', func.__name__)

    def __call__(self):
        print('> перед вызовом класса...', Decorator.__name__, "обертка функуии:", self.func.__name__)
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


add(10, 20)


class SimpleClass:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args):
        """
        Обращение к экземпляру как к функции
        :param args:
        :return:
        """
        print(self.name, args)


B = SimpleClass('Masha')

B(20)

