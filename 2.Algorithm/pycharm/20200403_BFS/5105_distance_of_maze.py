dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(v):
    global visit
    q = [v]
    visit[v[0]][v[1]] = 1
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not visit[nr][nc]:
                if arr[nr][nc] == 3:
                    return visit[r][c] - 1
                if arr[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c] + 1
                    q.append([nr, nc])
    return 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[1] * (N + 2)] + [[1] + list(map(int, input())) + [1] for _ in range(N)] + [[1] * (N + 2)]
    visit = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if arr[i][j] == 2:
                v = [i, j]
    result = bfs(v)
    print('#{} {}'.format(tc, result))

