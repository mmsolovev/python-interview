"""
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в
словаре для него должно сохраняться значение None. Если есть  значения, которым не хватило ключей, их необходимо
отбросить.
"""

list_keys = [f'key_{i}' for i in range(1, 11)]
list_values = [f'value_{j}' for j in range(1, 13)]

print(list_keys)
print(list_values)


def dict_maker(keys, values):
    if len(keys) > len(values):
        new_dict = dict.fromkeys(keys)
        for i in range(len(values)):
            new_dict[keys[i]] = values[i]
        return new_dict
    else:
        return {i[0]: i[1] for i in zip(keys, values)}


print(dict_maker(list_keys, list_values))
