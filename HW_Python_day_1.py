# Python. HW_1

# 1) Создать переменную типа String
str1 = "this_is_string"
print(str1)


# 2) Создать переменную типа Integer
# int целые числа
a = int(255)
print(a)


# 3) Создать переменную типа Float
b = (0.1+0.1+0.3)
print(b)


# 4) Создать переменную типа Bytes
message = "Hello world"
# string with encoding 'utf-8'
byte_message = bytes(message, 'utf-8')
print(byte_message)

size = 5
a = bytes(size)
print(a)


# 5) Создать переменную типа List
empty_list = []
print(empty_list)

list1 = [1, 2, 3, 4]
print(list1)

list2 = [1, "two", "&&", 4]
print(list2)

list2 = [1, "two", "@@", 4]
print(list2[3])

list3 = ["masses_1", ["masses_2", "?!?!", 4]]
print(list3[1][0])


# 6) Создать переменную типа Tuple
empty_typle = ()
print(empty_typle, type(empty_typle))

tuple_1 = ("one", 2, "thr&&")
print(tuple_1, type(tuple_1))

tuple_2 = 5, "c@t", "house"
print(tuple_2, type(tuple_2))

tuple_3, tuple_4 = 3, 4,
print(tuple_3, tuple_4, type(tuple_4))
# Вопрос. Здесь class 'int', как преобразовать в type 'tuple' ?


# 7) Создать переменную типа Set
set_1 = {1, 5, 10}
print(set_1, type(set_1))

set_2 = {"meow", "me0w"}
print(set_2, type(set_2))

set_3 = {"double", 2, 2, "double"}
print(set_3, type(set_3))
# set cannot have duplicates

empty_set = set()
print(empty_set, type(empty_set))


# 8. Создать переменную типа Frozen set
example_1 = ("H", "e", "l", "l", "o")
fSet = frozenset(example_1)
print("Frozen set", example_1)
print("Empty set", ())
print(type(example_1))

froz_1 = frozenset([1, 2, 3, 4])
froz_2 = frozenset([3, 4, 5, 6])
froz_3 = froz_2.copy # .copy = копирование
froz_4 = frozenset(["one", "two", 3, 6])
print(froz_3)
print(froz_1.union (froz_2))
# .union = объединение
print(froz_1.intersection(froz_4))
# .intersection = пересечения
print(froz_1.difference(froz_4))
print(froz_4.difference(froz_1))
# .difference = различия
print(froz_1.symmetric_difference(froz_2))
print(froz_1.symmetric_difference(froz_4))
# .symmetric_difference = все не одинаковые символы


# 9) Создать переменную типа Dict
dict_town = [['moskva', 495], ['piter', 'number'], ['penza', 8412]]
get_dict = dict(dict_town)
print(type(dict_town), get_dict, type(get_dict))
# переменная d3_list - содержит список,
# переменной get_dict преобразуем в type dict

dict_1 = dict.fromkeys(['a', 'b', 'c'], 100)
print(dict_1, type(dict_1))
# fromkeys - методу передаётся список, в котором содержатся ключи
# данный метод исп. тогда, когда требуется приватизировать ключи к определенным значениям

empty_dict = {}
print(empty_dict, type(empty_dict))

#     key: 'value'
dict_2 = {1: 'one', 2: 222, 3: [1, 2, 3], 'key_01': 'key text'}
print(dict_2, type(dict_2))
print(dict_2['key_01'])  # Метод обращения к ключу ['key_01']. Output: key text.

dict_3 = {1: 'one', 2: 'two', 3: 'three'}
dict_3[4] = 'four'  # добавление новой пары в словаре
dict_3['number'] = 'onetworhree'
print(dict_3, type(dict_3))
print(dict_3[4], dict_3['number'])
# [] - вызов значения
dict_3[3] = 'ТРИ'
print(dict_3)

dict_del = {1: 'one', 2: 'two', 3: 'three'}
print(dict_del)
del dict_del[2]  # удаление пары 2
print(dict_del)

dict5 = {1: 'one', 2: 'two', 3: 'three'}
print(dict5)
print(len(dict5))  # подсчет количества пар значений
print(1 in dict5, 5 in dict5, 7 not in dict5)


# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
str1 = ("one")
str2 = ("two")
print(str1 + str2, type(str))


# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
num1=int(10)
num2=int(20)
print(num1 + num2, type(num1))


# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
num1=int(1890)
num2=int(2)
print(num1 / num2, type(num2))


# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
num1=int(2.5)
num2=int(2)
print(num1 * num2, type(num2))


# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
num1=int(90)
num2=int(45)
print(num1 // num2, type(num2))


# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
num1=int(10)
num2=int(3)
print(num1 % num2, type(num1))

print(26 % 7)
# 26-(7+7+7)=5
# Output: 5
print(5 % 10)
print(5 % 0.25)
print(10 % 3)


#17) отменено

#Выгрузить файл в Git репозиторий.