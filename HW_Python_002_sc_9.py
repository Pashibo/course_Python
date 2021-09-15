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