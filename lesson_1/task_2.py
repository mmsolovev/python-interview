"""
Реализовать функцию print_directory_contents(path). Функция принимает имя директории и выводит ее содержимое, включая
содержимое всех поддиректории (рекурсивно вызывая саму себя). Использовать os.walk нельзя, но можно использовать
os.listdir и os.path.isfile
"""

import os


def print_directory_contents(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        print(i)
        if not os.path.isfile(f'{path}/{i}'):
            print_directory_contents(f'{path}/{i}')


# print_directory_contents()
