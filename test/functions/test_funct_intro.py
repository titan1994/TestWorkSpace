from pprint import pprint


def show_abc(a: 'spam', b: (1, 10), c: float) -> int:
    print(a, b, c)


pprint(dir(show_abc.__code__))

pprint(show_abc.__code__.co_varnames)
pprint(show_abc.__annotations__)