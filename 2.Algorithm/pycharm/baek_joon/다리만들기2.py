def instack(n, m):



N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
id = 0
for n in range(N):
    for m in range(M):
        if matrix[n][m] == 1:
            id += 1