# # Python.Homework_  # 2
#
# # 1) Создать 2 переменных типа String с разными значениями
a = 'Hello'
b = 'World'
print(a, b, type(a))
#
# # 2) Создать 4 переменных типа Integer с разными значениями
n_1 = 123
n_2 = 345
n_3 = 678
n_4 = 321
print(n_1, n_2, n_3, n_4, type(n_1), type(n_4))
#
# # 3) Создать 3 переменных типа Float с разными значениями
f_1 = 546.67
f_2 = 445.54
f_3 = 4588.901
print(f_1, type(f_1), f_2, type(f_2), f_3, type(f_3))
#
# # 4) Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
i_01 = 1
i_02 = 10
i_03 = 55
i_04 = 70
i_05 = 75
i_06 = 2
print('-- i_01 =', i_01 < i_02, '-- i_02 =', i_01 > i_02, '-- i_03 =', i_01 >= i_02)
print('-- i_04 =', i_01 <= i_02, '-- i_05 =', i_01 != i_02, '-- i_06 =', i_06 < i_02)
print('-- i_07 =', i_06 < i_02, '-- i_08 =', i_03 > i_05, '-- i_09 =', i_04 < i_03)
print('-- i_10 =', i_05 > i_06, '-- i_11 =', i_06 != i_05, '-- i_12 =', i_01 <= i_03)
print('-- i_13 =', i_04 >= i_02, '-- i_14 =', i_01 < i_04, '-- i_15 =', i_05 != i_02)
#
# # 5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты вевести в консоль.
ff_01 = 1.001
ff_02 = 1.003
ff_03 = 55.550
ff_04 = 71.022
ff_05 = 71.021
ff_06 = 100.001
print('-- ff_01 =', ff_01 < ff_02, '-- ff_02 =', ff_01 > ff_02, '-- ff_03 =', ff_01 >= ff_02)
print('-- ff_04 =', ff_01 <= ff_02, '-- ff_05 =', ff_01 != ff_02, '-- ff_06 =', ff_06 < ff_02)
print('-- ff_07 =', ff_06 < ff_02, '-- ff_08 =', ff_03 > ff_05, '-- ff_09 =', ff_04 < ff_03)

# # 6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты высвести в консоль.
i_01 = 1
i_02 = 10
i_03 = 55
i_04 = 70
i_05 = 75
i_06 = 2
print(i_01 < i_02 or i_01 > i_02)
print(i_01 >= i_02 and i_01 > i_02)
not (i_01 < i_02 and i_02 < i_03)
not (i_01 > i_02 and i_02 > i_03)
print(i_06 < i_02 and i_04 < i_03)
print(i_06 < i_02, not i_03 > i_05)
print(i_04 < i_03 and i_05 != i_02)
print(i_05 > i_06 or i_06 != i_05)
print(i_01 <= i_03 or i_05 == i_02)
not (i_05 != i_02 or i_04 < i_01)

# # 7) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"

a = int(input())
if a <= 30:
    print('Вы ввели число =', a)

# # 8) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"

import random

a = int(input())
b = random.randint(1, 100)
if a < b:
    print('Вы ввели число =', a, 'которое <', b)
elif a > b:
    print('Вы ввели число =', a, 'которое >', b)
if a == b:
    print('Вы ввели число =', a, 'которое =', b)

# # 9) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомных 2 целых числа (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое
#     (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"

import random
c = int(input())
d = random.randint(1, 100)
e = random.randrange(1, 101, 1)

if c < d and c < e:
    print('Вы ввели число =', c, 'которое <', d, 'и <', e)
elif c < d and c > e:
    print('Вы ввели число =', c, 'которое <', d, 'и >', e)
elif c < d and c == e:
    print('Вы ввели число =', c, 'которое <', d, 'и =', e)

if c > d and c < e:
    print('Вы ввели число =', c, 'которое >', d, 'и <', e)
elif c > d and c > e:
    print('Вы ввели число =', c, 'которое >', d, 'и >', e)
elif c > d and c == e:
    print('Вы ввели число =', c, 'которое >', d, 'и =', e)

if c == d and c < e:
    print('Вы ввели число =', c, 'которое =', d, 'и <', e)
elif c == d and c > e:
    print('Вы ввели число =', c, 'которое =', d, 'и >', e)
elif c == d and c == e:
    print('Вы ввели число =', c, 'которое =', d, 'и =', e)

# Комментарии - подсказки по теме для личного пользования
# import random будет импортировать случайный модуль, тогда как from random import random
# будет специально импортировать случайную функцию из модуля.
# import random включает модуль в пространство имен под именем random.
# from random import random включает функцию 'random' из пространства имен random в глобальное пространство имен.
#
# Итак, в первом примере вы должны вызвать random.random, а во втором - random.
# Оба получат доступ к одной и той же функции.
# Сходным образом, from random import randint будет импортировать randint в глобальное пространство имен,
# поэтому вы можете просто вызвать randint вместо random.randint.
#
# import random
# a = random.random()
# b = random.randint(1, 5)
# # you can call any function from the random module using random.<function>
#
# или...
#
# from random import random, randint
# # add any other functions you need here
# a = random()
# b = randint(1, 5)
# # those function names from the import statement are added to your namespace
