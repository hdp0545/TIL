dy = [1, 0, 0, -1]
dx = [0, -1, 1, 0]
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            location = [i, j]
shark = [2, 0]
deque()



