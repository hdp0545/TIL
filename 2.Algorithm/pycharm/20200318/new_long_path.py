def f(i, s):
    global result
    visit[i] = 1
    for j in ad_list[i]:
        if visit[j] == 0:
            f(j, s + 1)
            visit[j] = 0
    if s > result:
        result = s


for tc in range(int(input())):
    n, m = map(int, input().split())
    ad_list = [[] for _ in range(n + 1)]
    for i in range(m):
        s, e = map(int, input().split())
        ad_list[s].append(e)
        ad_list[e].append(s)
    result = 1
    for i in range(1, n + 1):
        visit = [0] * (n + 1)
        f(i, 1)
    print('#{} {}'.format(tc + 1, result))