def strangesort(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if i % 2:
                min = i
                if a[min] > a[j]:
                    min = j
                a[i], a[min] = a[min], a[i]
            else:
                max = i
                if a[max] < a[j]:
                    max = j
                a[i], a[max] = a[max], a[i]
    return a


for test_case in range(1, int(input()) + 1):
    N = int(input())
    N_list = list(map(int, input().split()))
    result = list(map(str, strangesort(N_list)))
    print('#{} {}'.format(test_case, ' '.join(result[0:10])))