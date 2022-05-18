for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    ad_list = [[] for _ in range(N+1)]
    for i in range(M):
        ad_list[data[2*i]] += [data[2*i + 1]]
        ad_list[data[2*i + 1]] += [data[2*i]]
    visit = [True] * (N + 1)
    result = 0
    for i in range(1, N+1):
        if visit[i]:
            visit[i] = False
            stack = [i]
            while stack:
                n = stack.pop()
                for j in ad_list[n]:
                    if visit[j]:
                        stack.append(j)
                        visit[j] = False
            result += 1
    print(f'#{tc} {result}')

