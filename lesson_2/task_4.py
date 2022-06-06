"""
Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна передаваться переменная —
скидка), и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и возвращаться
результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский
классы (вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:

    def __init__(self, price=300):
        self.__name = "Product"
        self.__price = price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, price, discount):
        super().__init__(price)
        self.discount = discount

    def __str__(self):
        return f'{self._ItemDiscount__price - self._ItemDiscount__price * self.discount}'

    def get_parent_data(self):
        print(f'{self._ItemDiscount__name} {self._ItemDiscount__price}')


a = ItemDiscount()
b = ItemDiscountReport(500, 0.1)

print(b)
