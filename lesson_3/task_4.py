"""
Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
Необходимо открыть файл и создать два списка: с текстовой и числовой информацией. Для создания списков использовать
генераторы. Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть обработан и
записан в файл таким образом, чтобы каждая строка файла содержала текстовое и числовое значение
(например example345). Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого.
"""

from os import path


def file_maker():
    try:
        f = open('text.txt', 'x')
        list_text = ['example' for _ in range(10)]
        list_nums = [i for i in range(10)]
        words = zip(list_text, list_nums)
        for word in words:
            f.write(f'{word[0]}{word[1]}\n')
        f.close()
    except FileExistsError:
        print('Файл уже существует')


def file_reader(file_path):
    f = open(file_path, 'r')
    for line in f:
        print(line)


file_maker()
file_reader(path.abspath('text.txt'))
