"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе будет
отвечать за вывод названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
"""


class ItemDiscount:

    def __init__(self, price=300):
        self.__name = "Product"
        self.__price = price


class ItemNameReport(ItemDiscount):

    def get_info(self):
        print(f'{self._ItemDiscount__name}')


class ItemPriceReport(ItemDiscount):

    def get_info(self):
        print(f'{self._ItemDiscount__price}')


a = ItemNameReport()
b = ItemPriceReport()

a.get_info()
b.get_info()
