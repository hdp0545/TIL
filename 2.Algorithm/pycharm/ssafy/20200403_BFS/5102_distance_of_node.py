def bfs(v, goal):
    global visit
    q = [v]
    visit[v] = 1
    while q:
        t = q.pop(0)
        for g in ad_list[t]:
            if not visit[g]:
                if g == goal:
                    return visit[t]
                else:
                    visit[g] = visit[t] + 1
                    q.append(g)
    return 0


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    ad_list = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        ad_list[v1].append(v2)
        ad_list[v2].append(v1)
    S, G = map(int, input().split())
    result = bfs(S, G)
    print('#{} {}'.format(tc, result))