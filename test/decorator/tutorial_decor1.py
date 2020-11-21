class Decorator:
    def __init__(self, func):
        """
        Args:
            func:
        """
        print('> РљР»Р°СЃСЃ Decorator РјРµС‚РѕРґ __init__')
        self.func = func
        print('Р¤СѓРєРЅС†РёСЏ РєРѕС‚РѕСЂСѓСЋ РјС‹ РѕР±РѕСЂР°С‡РёРІР°РµРј', func.__name__)

    def __call__(self):
        print('> РїРµСЂРµРґ РІС‹Р·РѕРІРѕРј РєР»Р°СЃСЃР°...', Decorator.__name__, "РѕР±РµСЂС‚РєР° С„СѓРЅРєСѓРёРё:", self.func.__name__)
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


add(10, 20)


class SimpleClass:
    def __init__(self, name):
        """
        Args:
            name:
        """
        self.name = name

    def __call__(self, *args):
        """РћР±СЂР°С‰РµРЅРёРµ Рє СЌРєР·РµРјРїР»СЏСЂСѓ РєР°Рє Рє С„СѓРЅРєС†РёРё
        :param args: :return:

        Args:
            *args:
        """
        print(self.name, args)


B = SimpleClass('Masha')

B(20)

