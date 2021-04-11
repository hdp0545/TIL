dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
result = 0
R, C = map(int, input().split())
arr = [[1] * (C+2)] + [[1] + list(map(str, input())) + [1] for _ in range(R)] + [[1] * (C+2)]
for i in range(1, R+1):
    for j in range(1, C+1):
        if arr[i][j] == 'L':
            visit = [[1] * (C + 2)] + [[1] + [0] * C + [1] for _ in range(R)] + [[1] * (C + 2)]
            q = [(i, j)]
            visit[i][j] = rear = 1
            front = 0
            while front != rear:
                r, c = q[front]
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if visit[nr][nc] == 0:
                        if arr[nr][nc] == 'L':
                            visit[nr][nc] = visit[r][c] + 1
                            q.append((nr, nc))
                            rear += 1
                front += 1
            r = visit[r][c] -1
            if result < r:
                result = r
print(result)



