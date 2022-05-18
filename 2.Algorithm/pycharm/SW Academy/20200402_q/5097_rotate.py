for tc in range(1, int(input()) + 1): #
    N, M = map(int, input().split())
    data = list(input().split())
    for _ in range(M):
        n = data.pop(0)
        data.append(n)
    print('#{} {}'.format(tc, data[0])


