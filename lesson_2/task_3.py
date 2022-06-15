"""
Реализовать возможность переустановки значения цены товара в родительском классе. Проверить, распечатать информацию о
товаре.
"""


class ItemDiscount:
    def __init__(self, price=300):
        self.__name = "Product"
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'{self._ItemDiscount__name} {self._ItemDiscount__price}')


a = ItemDiscount()
b = ItemDiscountReport()
c = ItemDiscountReport(500)

b.get_parent_data()
c.get_parent_data()
