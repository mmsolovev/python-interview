"""
Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
логики работы программы будет сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self):
        self.__name = "Product"
        self.__price = 300


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(f'{self._ItemDiscount__name} {self._ItemDiscount__price}')


a = ItemDiscount()
b = ItemDiscountReport()

b.get_parent_data()
