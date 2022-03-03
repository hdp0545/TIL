from collections import deque

dy = [1, 1, 0, -1, -1, -1, 0, 1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
woods = [list(map(int, input().split())) for _ in range(M)]
land = [[5] * N for _ in range(N)]
forest = [[deque([]) for _ in range(N)] for _ in range(N)]

for wood in woods:
    forest[wood[0]-1][wood[1]-1].append(wood[2])

for _ in range(K):
    # 봄
    for r in range(N):
        for c in range(N):
            i = 0
            for i in range(len(forest[r][c])):
                if land[r][c] < forest[r][c][i]:
                    i -= 1
                    break
                else:
                    land[r][c] -= forest[r][c][i]
                    forest[r][c][i] += 1

            for j in range(len(forest[r][c])-1, i, -1):
                land[r][c] += forest[r][c][j] // 2
                forest[r][c].pop()
    # 가을
    for r in range(N):
        for c in range(N):
            for wood in forest[r][c]:
                if wood % 5 == 0:
                    for i in range(8):
                        nr, nc = r + dy[i], c + dx[i]
                        if 0 <= nr < N and 0 <= nc < N:
                            forest[nr][nc].appendleft(1)
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]
result = 0
for r in range(N):
    for c in range(N):
        result += len(forest[r][c])
print(result)
#
#     while woods:
#         r, c, wood = woods.popleft()
#         if land[r][c] < wood:
#             dead_woods.append([r, c, wood])
#         else:
#             land[r][c] -= wood
#             wood += 1
#             grow_woods.append([r, c, wood])
#     # 여름
#     while dead_woods:
#         r, c, wood = dead_woods.pop()
#         land[r][c] += wood // 2
#
#     # 가을
#     while grow_woods:
#         r, c, wood = grow_woods.popleft()
#         if wood % 5 == 0:
#             for i in range(8):
#                 nr, nc = r+dy[i], c+dx[i]
#                 if 0 <= nr < N and 0 <= nc < N:
#                     woods.appendleft([nr, nc, 1])
#         woods.append([r, c, wood])
#     # 겨울
#     for i in range(N):
#         for j in range(N):
#             land[i][j] += A[i][j]
# print(len(woods))
#
