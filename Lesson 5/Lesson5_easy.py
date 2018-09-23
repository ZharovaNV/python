# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil
import re


def add_new_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(' Директория {} создана'.format(dir_path))
    except FileExistsError:
        print('Создание невозможно. Директория {} уже существует'.format(dir_path))


def add_dirs():
    for i in range(1, 10):
        add_new_dir('dir_{}'.format(i))


def remove_empt_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print('Директории {} удалена'.format(dir_path))
    except FileNotFoundError:
        print('Удаление невозможно, директории {} не существует'.format(dir_path))
    except OSError:
        print('Удаление невозможно, директория {} не пустая'.format(dir_path))


def remove_dirs():
    for i in range(1, 10):
        remove_empt_dir('dir_{}'.format(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def show_dir_or_file(showdir, showfile):
    for obj in os.listdir():
        fullname = os.path.join(os.getcwd(), obj)
        if os.path.isdir(fullname) and showdir:
            print(obj)
        if os.path.isfile(fullname) and showfile:
            print(obj)


def show_dirs():
    show_dir_or_file(True, False)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_work_file():
    cur_file = sys.argv[0]
    new_file = cur_file[:-3] + '_copy.' + cur_file[-2:]
    shutil.copyfile(cur_file, new_file)
    print('Создан файл', new_file)


# для задач normal

def is_name_correct(dirname):
    if re.search('^[A-Za-z_0-9]+$', dirname) is None:
        print('Некорректное имя папки')
        return False
    return True


def go_to_dir():
    new_dir = input('Введите имя папки:')
    if not is_name_correct(new_dir):
        return
    fullname = os.path.join(os.getcwd(), new_dir)
    try:
        os.chdir(fullname)
        print('Успешно перешел в папку {}'.format(fullname))
    except FileNotFoundError:
        print('Невозможно переайти в папку {}. Папки не найдено'.format(fullname))


def add_any_dir():
    new_dir = input('Введите имя папки:')
    if not is_name_correct(new_dir):
        return
    add_new_dir(new_dir)


def remove_any_empty_dir():
    new_dir = input('Введите имя папки:')
    if not is_name_correct(new_dir):
        return
    remove_empt_dir(new_dir)
