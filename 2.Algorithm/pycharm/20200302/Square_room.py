dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for t in range(1, int(input())+1):
    N = int(input())
    arr = [['*'] * (N+2)]
    arr += [['*'] + list(map(int, input().split())) + ['*'] for _ in range(N)]
    arr += [['*'] * (N+2)]
    r, r1 = 1, N ** 2
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] != '*':
                ni, nj, cnt, temp = i, j, 1, arr[i][j]
                while True:
                    for k in range(4):
                        if arr[ni + dy[k]][nj + dx[k]] == arr[ni][nj] - 1:
                            arr[ni][nj] =  '*'
                            ni, nj, cnt = ni + dy[k], nj + dx[k], cnt + 1
                            break
                    else:
                        st = arr[ni][nj]
                        arr[ni][nj] = '*'
                        break
                ni, nj, arr[i][j] = i, j, temp
                while True:
                    for k in range(4):
                        if arr[ni + dy[k]][nj + dx[k]] == arr[ni][nj] + 1:
                            arr[ni][nj] =  '*'
                            ni, nj, cnt = ni + dy[k], nj + dx[k], cnt + 1
                            break
                    else:
                        arr[ni][nj] = '*'
                        break
                if r < cnt:
                    r, r1 = cnt, st
                elif r == cnt:
                    r1 = min(r1, st)
    print('#{} {} {}'.format(t, r1, r))