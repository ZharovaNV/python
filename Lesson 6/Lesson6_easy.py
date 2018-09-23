# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(self.name, 'goes...')

    def stop(self):
        print(self.name, 'stops...')

    def turn(self, direction):
        if (direction in ['left', 'right']):
            print(self.name, 'turns to the', direction, '...')
        else:
            print('Direction not defined')

class SportCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police =  False

    def go(self):
        print(self.name, 'goes...')

    def stop(self):
        print(self.name, 'stops...')

    def turn(self, direction):
        if (direction in ['left', 'right']):
            print(self.name, 'turns to the', direction, '...')
        else:
            print('Direction not defined')



class WorkCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police  = False

    def go(self):
        print(self.name, 'goes...')

    def stop(self):
        print(self.name, 'stops...')

    def turn(self, direction):
        if (direction in ['left', 'right']):
            print(self.name, 'turns to the', direction, '...')
        else:
            print('Direction not defined')


class PoliceCar:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print(self.name, 'goes...')

    def stop(self):
        print(self.name, 'stops...')

    def turn(self, direction):
        if (direction in ['left', 'right']):
            print(self.name, 'turns to the', direction, '...')
        else:
            print('Direction not defined')

# car = SportCar('','','mnb',False)
# car.turn('left')

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(self.name, 'goes...')

    def stop(self):
        print(self.name, 'stops...')

    def turn(self, direction):
        if (direction in ['left', 'right']):
            print(self.name, 'turns to the', direction, '...')
        else:
            print('Direction not defined')

class TownCar(Car):
    pass

class SportCar(Car):

    pass


class WorkCar(Car):

    def do_some_work(self, kind_of_work):
        print(self.name, 'works... It makes', kind_of_work)

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

    def immerge_signal(self):
        print('Give way. Police car goes...')

