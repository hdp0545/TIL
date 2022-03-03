T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    ad_list = [[] for _ in range(E+2)]
    for i in range(0, 2*E, 2):
        ad_list[data[i]] += [data[i+1]]
    stack = [N]
    cnt = 0
    while stack:
        v = stack.pop()
        cnt += 1
        while ad_list[v]:
            stack += [ad_list[v].pop()]
    print(f'#{tc} {cnt}')