dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def f(n, i, j, cnt=1):
    global arr
    arr[i][j] = '*'
    for k in range(4):
        if arr[i + dy[k]][j + dx[k]] == n-1:
            cnt += 1
            f(n-1, i+dy[k], j+dx[k], cnt)
        if arr[i + dy[k]][j + dx[k]] == n+1:
            cnt += 1
            f(n+1, i+dy[k], j+dx[k], cnt)
    return cnt


for t in range(1, int(input())+1):
    N = int(input())
    arr = [['*'] * (N+2)]
    arr += [['*'] + list(map(int, input().split())) + ['*'] for _ in range(N)]
    arr += [['*'] * (N+2)]
    r = 1
    r1 = N ** 2
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] != '*':
                st = arr[i][j]
                cnt = f(arr[i][j], i, j)
                if r < cnt:
                    r, r1 = cnt, st
                elif r == cnt:
                    r1 = min(r1, st)
    print('#{} {} {}'.format(t, r1, r))
