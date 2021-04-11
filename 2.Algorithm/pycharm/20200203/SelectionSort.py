def selectionsort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a



a = [1, 2, 6, 3, 2134, 245, 79, 11, 6, 4]

print(selectionsort(a))