T = int(input())
for tc in range(1, T+1):
    N, M, E = map(int, input().split())
    ad_list = [0 for _ in range(N+1)]
    for _ in range(M):
        node, value = map(int, input().split())
        ad_list[node] = value
    result = 0
    stack = [E]
    while stack:
        v = stack.pop()
        if v <= N:
            if ad_list[v]:
                result += ad_list[v]
            else:
                stack += [2*v, 2*v + 1]
    print(f'#{tc} {result}')