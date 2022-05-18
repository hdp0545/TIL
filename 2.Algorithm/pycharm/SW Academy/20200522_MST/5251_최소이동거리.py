for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    ad_list = [[] for _ in range(N)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        ad_list[s].append([e, w])
    result = 10000000
    stack = [[0, 0]]
    while stack:
        n, temp = stack.pop()
        if n == N and result > temp:
            result = temp
        elif temp >= result:
            pass
        else:
            for target in ad_list[n]:
                stack.append([target[0], temp+target[1]])
    print(f'#{tc} {result}')

