"""
Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Считаем, что клиент вносит средства в последний день каждого месяца, кроме
первого и последнего. Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.
"""


def bank_deposit(deposit, months, some_sum):
    profit = 0
    if 1000 < deposit < 10000:
        if months == 6 or months >= 24:
            profit = 0.05
        elif months == 12:
            profit = 0.06
    elif 10000 <= deposit < 100000:
        if months == 6:
            profit = 0.06
        elif months == 12:
            profit = 0.07
        elif months >= 24:
            profit = 0.065
    elif 100000 <= deposit < 1000000:
        if months == 6:
            profit = 0.07
        elif months == 12:
            profit = 0.08
        elif months >= 24:
            profit = 0.075
    i = 1
    while i <= months:
        if i == 1 or i == months:
            deposit += deposit * (profit / 12)
            i += 1
        else:
            deposit += deposit * (profit / 12) + some_sum
            i += 1
    return deposit


print(bank_deposit(10000, 6, 1000))
print(bank_deposit(10000, 6, 0))
