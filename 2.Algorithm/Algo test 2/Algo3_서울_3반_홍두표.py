from itertools import combinations as comb
from collections import deque as dq

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
def bfs(sp1, sp2):
    copy_map = [m[:] for m in map]
    copy_map[sp1[0]][sp1[1]] = 3
    copy_map[sp2[0]][sp2[1]] = 4
    q = dq([sp1, sp2])
    minuete = 0
    while q:
        team_3, team_4 = q.popleft()
        for i in range(4):
            if copy_map[team_3[0]+dx[i]] != 1:
                if
                q.append()
        for j in range(4):
            if t

    return minuete




N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
start_points = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 2:
            start_points.append([i, j])
for start_point1, start_point2 in comb(start_points, 2):
    temp = bfs(start_point1, start_point2)
    if temp < result:
        result = temp
print(result)
