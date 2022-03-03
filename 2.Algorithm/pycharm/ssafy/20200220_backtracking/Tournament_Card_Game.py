def winner(a, b, lis):
    if lis[a] == lis[b]:
        return a
    return a if lis[a] - lis[b] == 1 or lis[a] - lis[b] == -2 else b


def tournament(i, j, lis):
    if i == j:
        return i
    if i + 1 == j:
        return winner(i, j, lis)
    return winner(tournament(i, (i+j)//2, lis), tournament((i+j)//2 + 1, j, lis), lis)


for test_case in range(1, int(input())+1):
    N = int(input())
    lis = list(map(int, input().split()))
    print('#{} {}'.format(test_case, tournament(0, N-1, lis)+1))
