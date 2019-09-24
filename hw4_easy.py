# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random


random_list = [random.randint(-10, 10) for _ in range(5)]
sqrt_list = [a ** 2 for a in random_list]
# sqrt_list = list(map(lambda a: a ** 2, random_list))  - через лямбда-функцию
print(random_list, '-->', sqrt_list)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# пустая строка + отделяющая линия
print()
print('_' * 100)
print()

fruits1 = ['яблоко', 'груша', 'банан', 'персик', 'абрикос', 'киви', 'апельсин']
fruits2 = ['инжир', 'нектарин', 'яблоко', 'слива', 'киви', 'банан']
print(fruits1)
print(fruits2)

same_fruits_list = [fruit for fruit in fruits1 if fruit == fruit in fruits2]
print(same_fruits_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# пустая строка + отделяющая линия
print()
print('_' * 100)
print()

random_list = [random.randint(-100, 100) for _ in range(20)]
print('Произвольный список:', random_list)

new_list = [a for a in random_list if a % 3 == 0 and a > 0 and a // 4 != a / 4]

print('Искомый список:', new_list)