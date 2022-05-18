
def selectionsort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

a = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]
N = len(a)
a_list = []
for i in a:
    a_list.extend(i)

a_list = selectionsort(a_list)



matrix = [[0]*N for _ in range(N)]
value = 0
for cnt in range(2*N - 1):
    s = cnt // 4
    for i in range((2*N - cnt) // 2):
        if cnt % 4 == 0:
            matrix[s][s + i] = a_list[value]
            value = value + 1
        elif cnt % 4 == 1:
            matrix[s+1+i][(N-1) - s] = a_list[value]
            value = value + 1
        elif cnt % 4 == 2:
            matrix[(N-1) - s][(N-2) - s - i] = a_list[value]
            value = value + 1
        else:
            matrix[(N-2) - s - i][s] = a_list[value]
            value = value + 1
print(matrix)