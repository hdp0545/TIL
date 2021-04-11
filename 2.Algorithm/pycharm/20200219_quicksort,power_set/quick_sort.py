def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while a[L] < a[pivot] and L < R:
            L += 1
        while a[R] >= a[pivot] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


def quicksort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quicksort(a, begin, p-1)
        quicksort(a, p+1, end)
    return a


a = [3, 2, 5, 2, 10]
quicksort(a, 0, 4)
print(a)