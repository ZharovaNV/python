# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player = {'name': 'Alex', 'health': 100, 'damage': 50}
enemy = {'name': 'Piter', 'health': 100, 'damage': 50}


def attack(attacker, attacked):
    attacked['health'] -= attacker['damage']

# print(player, enemy)
#
# attack(player, enemy)
# print(player, enemy)
#
# attack(enemy, player)
# print(player, enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

# Создание файлов
player = {'name': 'Alex', 'health': 140, 'damage': 40, 'armor': 1.4}
enemy = {'name': 'Piter', 'health': 100, 'damage': 50, 'armor': 1.2}

def create_file(person):
    with open('{}.txt'.format(person['name']), 'w', encoding='UTF-8') as file:
        for key, value in person.items():
            file.write('{} - {}\n'.format(key, value))

create_file(player)
create_file(enemy)


# Чтение файлов и создание словарей
def create_person(file):
    person = {}
    with open(file, 'r', encoding='UTF-8') as file:
        for line in file:
            snm, val = line.strip().split(' - ')
            if snm != 'name':
                person[snm] = float(val)
            else:
                person[snm] = val
    return person


def print_info(role, person):
    print(role, person['name'], 'здоровье:', person['health'], 'ущерб:', person['damage'], 'броня:',
          person['armor'])

player = create_person('Alex.txt')
enemy = create_person('Piter.txt')
print_info('Игрок:', player)
print_info('Враг', enemy)

# Игровая сессия
def get_damage(damage, armor):
    return damage / armor

def attack(attacker, attacked):
    attacked['health'] -= get_damage(attacker['damage'], attacked['armor'])

while player['health'] > 0 and enemy['health'] > 0:
    attack(enemy, player)
    # print(player, enemy)
    if player['health'] <= 0:
        print('Победитель: {}, {} единиц здоровья'.format(enemy['name'], enemy['health']))
        break
    attack(player, enemy)
    # print(player, enemy)
else:
    print('Победитель: {}, {} единиц здоровья'.format(player['name'], round(player['health'], 2)))