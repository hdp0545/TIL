def binarySearch(page, key):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        middle = (start + end) // 2
        if middle == key:
            return cnt + 1
        elif middle > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1
    return False



for test_case in range(1, int(input()) + 1):
    P, Pa, Pb = (map(int, input().split()))

    if binarySearch(P, Pa) < binarySearch(P, Pb):
        result = 'A'
    elif binarySearch(P, Pa) > binarySearch(P, Pb):
        result = 'B'
    else:
        result = '0'
    print('#{} {}'.format(test_case, result))