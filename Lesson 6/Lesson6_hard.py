# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Toy:

    def __init__(self, name, colour, type):
        self.name = name
        self.colour = colour
        self.type = type

class Factory(Toy):

    def _buy_material(self):
        print('Закупаем серье для игрушки {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def _sew(self):
        print('Шьем игрушку {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def _paint(self):
        print('Красим игрушку {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def make_toy(self):
        self._buy_material()
        self._sew()
        self._paint()
        return Toy(self.name, self.colour, self.type)

obj = Factory('Крокодил', 'зеленый', 'животное').make_toy()
print(type(obj))

# Либо если требовалось создание объекта внутри функции
class Factory:

    def __init__(self, name, colour, type):
        self.name = name
        self.colour = colour
        self.type = type

    def _buy_material(self):
        print('Закупаем серье для игрушки {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def _sew(self):
        print('Шьем игрушку {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def _paint(self):
        print('Красим игрушку {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def make_toy(self):
        self._buy_material()
        self._sew()
        self._paint()
        class Toy(Factory):
            pass
        return Toy(self.name, self.colour, self.type)


obj = Factory('Крокодил', 'зеленый', 'животное').make_toy()
print(type(obj))


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка



class Toy:

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

class AnimalToy(Toy):

    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.type = 'животное'


class PersonToy(Toy):

    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.type = 'персонаж'

class Factory(Toy):

    def __init__(self, name, colour, type):
        super().__init__(name, colour)
        self.type = type

    def _buy_material(self):
        print('Закупаем серье для игрушки {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def _sew(self):
        print('Шьем игрушку {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def _paint(self):
        print('Красим игрушку {} цвета {} типа {}'.format(self.name, self.colour, self.type))

    def make_toy(self):
        self._buy_material()
        self._sew()
        self._paint()
        if self.type == 'животное':
            return AnimalToy(self.name, self.colour)
        elif self.type == 'персонаж':
            return PersonToy(self.name, self.colour)
        else:
            print('Игрушки такого типа на фабрике не производятся')


obj = Factory('Крокодил', 'зеленый', 'животное').make_toy()
print(type(obj))
