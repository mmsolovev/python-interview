"""
Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, целое
оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они совпадают,
программа должна возвращать значение True, иначе False.
"""


def num_check():
    num = input('Введите число')
    try:
        int(num)
        print('Число целое')

    except ValueError:
        try:
            float(num)
            print('Число дробное')
            if str(num).split('.')[0] == str(num).split('.')[1]:
                return True
            else:
                return False
        except ValueError:
            print('Не число')


print(num_check())
