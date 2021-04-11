from itertools import combinations as comb
from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(queue):
    visit = [[0]*M for _ in range(N)]
    q = deque(queue)
    cnt = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 0 and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    cnt += 1
                    q.append((nr, nc))
                    if cnt >= result:
                        return result
    return cnt


N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
wall_case = [(i, j) for i in range(N) for j in range(M) if maze[i][j] == 0]
number_zero = len(wall_case)
dq = [(i, j) for i in range(N) for j in range(M) if maze[i][j] == 2]
result = N * M
for walls in comb(wall_case, 3):
    arr = [m[:] for m in maze]
    for wi, wj in walls:
        arr[wi][wj] = 1
    result = bfs(dq)
print(number_zero - result - 3)
