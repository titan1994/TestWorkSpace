class A:
    def go(self):
        print('Go, A!')


class B(A):
    def go(self, name):
        """
        Args:
            name:
        """
        print('Go, {}!'.format(name))

a = A()
a.go()

b = B()
b.go('no')


class As:
    def __init__(self, name):
        """
        Args:
            name:
        """
        self.name = name



import math

class Vector2D:
    def __init__(self, x, y):
        """
        Args:
            x:
            y:
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

x = Vector2D(3, 4)
y = Vector2D(5, 6)

print(x+y)