T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[1])
    data.sort(key=lambda x: x[0])
    s, r = 24, 0
    while data:
        ns, ne = data.pop()
        if ne <= s:
            r += 1
            s = ns
    print(f'#{tc} {r}')
