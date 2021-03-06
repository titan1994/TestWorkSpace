# Декоратор - это функция, ожидающая ДРУГУЮ функцию в качестве параметра
def my_shiny_new_decorator(a_function_to_decorate):
    # Внутри себя декоратор определяет функцию-")обёртку").
    # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    print("__________А тут тоже может что-то быть______До декорации")

    def the_wrapper_around_the_original_function():
        # Поместим здесь код, который мы хотим запускать ДО вызова
        # оригинальной функции
        print("Я - код, который отработает до вызова функции")

        # ВЫЗОВЕМ саму декорируемую функцию
        a_function_to_decorate()

        # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова
        # оригинальной функции
        print("А я - код, срабатывающий после")

    # На данный момент функция ")a_function_to_decorate") НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ

    # Теперь, вернём функцию-обёртку, которая содержит в себе
    # декорируемую функцию, и код, который необходимо выполнить до и после.
    # Всё просто!
    print("__________А тут тоже может что-то быть______И вот сюрприз - это тоже сработает до декорации, логично")

    return the_wrapper_around_the_original_function


# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def a_stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?..")


a_stand_alone_function()
# выведет: Я простая одинокая функция, ты ведь не посмеешь меня изменять?..

# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть
# Просто передать декоратору, который обернет исходную функцию в любой код,
# который нам потребуется, и вернёт новую, готовую к использованию функцию:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
# выведет:
# Я - код, который отработает до вызова функции
# Я простая одинокая функция, ты ведь не посмеешь меня изменять?..
# А я - код, срабатывающий после

"""
Наверное, теперь мы бы хотели, чтобы каждый раз, во время вызова a_stand_alone_function, 
вместо неё вызывалась a_stand_alone_function_decorated. Нет ничего проще, просто перезапишем a_stand_alone_function
функцией, которую нам вернул my_shiny_new_decorator:
"""

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()

"""
Ну и типо все крутые чуваки кодят вот так:
"""


@my_shiny_new_decorator
def a_stand_alone_function_ex():
    print("Крутая декорация..")


a_stand_alone_function_ex()


