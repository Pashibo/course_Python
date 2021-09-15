import random
a = int(input())
b = random.randint(1, 100)
if a < b:
    print('Вы ввели число =', a, 'которое <', b)
elif a > b:
    print('Вы ввели число =', a, 'которое >', b)
if a == b:
    print('Вы ввели число =', a, 'которое =', b)