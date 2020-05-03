opr = (input('Введите значения через пробел\n'))

lst = opr.split(' ')

posk = (input('Введите искомое значение\n'))

def poisk(a, b):
    lst2 = []
    for i in a:
        lst2 = a.count(b)
    return lst2

print(poisk(lst, posk))