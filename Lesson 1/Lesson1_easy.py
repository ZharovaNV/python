print('Задача 1')

var1 = 10
var2 = int(input('Введите число:'))
print('(10 + ', var2, ') * 2 = ', (var1 + var2) *2)
name = input('Введите Ваше имя:')
print('Добрый день,', name)

print('Задача 2')
number = int(input('Введите число:'))
number += 2
print('Введенное Вами число плюс 2 равно', number)

print('Задача 3')
age = int(input('Введите Ваш возраст:'))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')