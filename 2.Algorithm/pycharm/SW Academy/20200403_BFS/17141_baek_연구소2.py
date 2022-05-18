from itertools import combinations as comb
from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(queue):
    visit = [[0]*N for _ in range(N)]
    for qi, qj in queue:
        visit[qi][qj] = 1
    q = deque(queue)
    cnt = 0
    depth = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != 1 and visit[nr][nc] == 0:
                    depth = visit[r][c] + 1
                    if depth >= result:
                        return result
                    q.append((nr, nc))
                    cnt += 1
                    visit[nr][nc] = depth
    if cnt == num_zero:
        return depth
    else:
        return result


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
start_case = [(i, j) for i in range(N) for j in range(N) if lab[i][j] == 2]
num_zero = len(['0' for i in range(N) for j in range(N) if lab[i][j] == 0]) + len(start_case) - M
result = N * N
for start_points in comb(start_case, M):
    arr = [m[:] for m in lab]
    result = bfs(list(start_points))
if result == N * N:
    print('-1')
else:
    print(result - 1)