# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print('Задача 1')
fruits = ["яблоко", "банан", "киви", "арбуз"]
maxlen = 0
for fruit in fruits:
    if len(fruit) > maxlen:
        maxlen = len(fruit)

# вариант с format
for index, fruit in enumerate(fruits, start=1):
    print('{}. {:>{}}'.format(index, fruit, maxlen))

# вариант с rjust
for index, fruit in enumerate(fruits, start=1):
    print('{}. {}'.format(index, fruit.rjust(maxlen, ' ')))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('\nЗадача 2')
list1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
list2 = [2, 2, 4, 4, 6, 6, 8, 8]
print ('Список 1:', list1)
print ('Список 2:', list2)

# reversed использовано из-за того что при удалении элементы сдвигаются влево.
for element in reversed(list1):
    if element in list2:
        list1.remove(element)
print('Итоговый список: ', list1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('\nЗадача 3')
list = [1, 2, 3, 4, 5, 6, 7, 8]
newlist = []
for element in list:
    if element % 2 == 0:
        newlist.append(element / 4)
    else:
        newlist.append(element * 2)
print('Исходный список:', list)
print('Новый список:', newlist)