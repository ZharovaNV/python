# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def human_info (name, age, town):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, town)

print(human_info('Василий','21','Москва'))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# Вариант 1
def my_max (n1, n2, n3):
    return max(n1, n2, n3)

print(my_max(6,-2,3))

# Вариант 2
f = (lambda n1, n2, n3: max(n1, n2, n3))

print(f(6,-2,3))

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def my_max_len (*args):
    return max(args, key = len)

print(my_max_len('aaa','bb','c'))