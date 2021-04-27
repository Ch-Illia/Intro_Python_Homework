# Задание №1
# Дан список словарей persons в формате с именами и возрастом:
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
from collections import defaultdict
coaches = [{"name": "Andriy Shevchenko", "age": 44},
           {"name": "Diego Simeone", "age": 51},
           {"name": "Frank Lampard", "age": 42},
           {"name": "Thomas Tuchel", "age": 47},
           {"name": "Andrea Pirlo", "age": 41},
           {"name": "Julian Nagelsmann", "age": 33},
           {"name": "Mauricio Pochettino", "age": 49},
           {"name": "Mikel Arteta", "age": 39},
           {"name": "Zinedine Zidane", "age": 48},
           {"name": "Jurgen Klopp", "age": 53},
           {"name": "Carlo Ancelotti", "age": 61},
           {"name": "Jose Mourinho", "age": 58}]

age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []

for c in coaches:
    name = c['name']
    age = c['age']
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)

min_age = min(age_by_names)
print('min_age:', *age_by_names[min_age])

max_len_name = max(len_name_by_names)
print('max_len_name:', *len_name_by_names[max_len_name])

print('average:', sum(ages) // len(ages))
#####
# Задание №2
# Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение},
# для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
#   - если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#   - если ключ есть в двух словарях -
#       поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]}.
