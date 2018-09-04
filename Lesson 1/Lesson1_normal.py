print('Задача 1')
number = int(input('Введите число:'))
while number <= 0 or number >= 10:
    print('Неверное число!')
    number = int(input('Введите число, которое больше 0, но меньше 10:'))
print(number, '- верное число!')

print('')
print('Задача 2')
number1 = int(input('Введите первое число:'))
number2 = int(input('Введите второе число:'))
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print('Второе число:', number1)
print('Первое число:', number2)
	