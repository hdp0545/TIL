for test_case in range(1, int(input())+1):
    L, U, X = (map(int, input().split()))
    if X < L:
        result = L - X
    elif X < U:
        result = 0
    else:
        result = -1
    print('#{} {}'.format(test_case, result))