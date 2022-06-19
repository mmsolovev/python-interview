"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове
функции в качестве аргумента должно передаваться путь и имя файла с расширением. В функции необходимо реализовать
поиск имени файла (с расширением), а затем «выделение» имени файла (без расширения). Расширений может быть несколько
(например testfile.tar.gz).
"""
import os


def get_file(path, name):
    if name in os.listdir(path):
        print(os.path.split(os.path.join(path, name))[1].split('.')[0])
    else:
        print('Нет такого файла по этому пути')


get_file('/Users/mmsolovev/PycharmProjects/python-interview/lesson_3', 'task_1.py')
