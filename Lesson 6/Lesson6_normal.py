# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def print_param(self):
        print(f'{self.name}: здоровье {self.health}, ущерб {self.damage}, броня {self.armor}')

    def _calc_damage(self, opponent_armor):
        damage = self.damage // opponent_armor
        return damage

    def person_attack(self, person):
        person.health -= self._calc_damage(person.armor)

class Player(Person):
    pass

class Enemy(Person):
    pass




class Battle:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def attack(self, player_attack):
        if player_attack:
            self.player.person_attack(self.enemy)
            print('{} нанес урон {} , у того осталось {} жизней.'.format(self.player.name, self.enemy.name, self.enemy.health))
        else:
            self.enemy.person_attack(self.player)
            print('{} нанес урон {} , у того осталось {} жизней.'.format(self.enemy.name, self.player.name,
                                                                         self.player.health))


player = Player('Ivan', 140, 30, 1.1)
enemy = Enemy('Oleg', 100, 50, 1.2)
player.print_param()
enemy.print_param()

player_attack = True
battle = Battle(player, enemy)
while player.health > 0 and enemy.health > 0:
    battle.attack(player_attack)
    player_attack = not(player_attack)


if player.health > 0:
    print('{} победил!'.format(player.name))
else:
    print('{} победил!'.format(enemy.name))

