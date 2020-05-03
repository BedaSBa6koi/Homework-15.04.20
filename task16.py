lst1 = [5, 7, 12, 0, -55, 3, -1, 0, 649, -1000, 0]
lst2 = []

def replacement():
    for i in lst1:
        if i < 0:
            lst2.append(-1)
        elif i > 0:
            lst2.append(1)
        else:
            lst2.append(0)
    print(lst1)
    print(lst2)

replacement()