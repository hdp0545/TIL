def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


import random
for _ in range(10):
    a = []

    for i in range(4):
        a.append()

    print(BubbleSort(a))