from itertools import combinations as comb
from collections import deque

dy = [0, -1, 0]
dx = [-1, 0, 1]


def death_cnt(r, c):
    global death
    global eliminate_data
    if death[r][c]:
        return 0
    else:
        death[r][c] = 1
        eliminate_data.append((r, c))
        return 1


def shooting(position, D):
    if arr[position[0]][position[1]]:
        return death_cnt(position[0], position[1])
    q = deque([position])
    visit = [[0] * M for _ in range(N)]
    visit[position[0]][position[1]] = 1
    while q:
        r, c = q.popleft()
        depth = visit[r][c] + 1
        if depth > D:
            return 0
        for i in range(3):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc]:
                    return death_cnt(nr, nc)
                q.append((nr, nc))
                visit[nr][nc] = depth


N, M, D = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
castle = [i for i in range(M)]
result = 0
for positions in comb(castle, 3):
    arr = [d[:] for d in data]
    death = [[0] * M for _ in range(N)]
    eliminate_data = []
    cnt = 0
    for j in range(N-1, -1, -1):
        for position in positions:
            cnt += shooting((j, position), D)
        for ei, ej in eliminate_data:
            arr[ei][ej] = 0
    if result < cnt:
        result = cnt
print(result)