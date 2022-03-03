def triangle(ad_list, N, i, j, k=1):
    result = 0
    if k == 3:
        if i in ad_list[j]:
            return 1
        return 0
    for ni in ad_list[i]:
        result += triangle(ad_list, N, ni, j, k+1)
    return result


for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    ad_list = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        ad_list[x] += [y]
    result = 0
    for i in range(1, N-1):
        j = i
        result += triangle(ad_list, N, i, j)
    print(f'#{test_case} {result}')
