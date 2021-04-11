from itertools import combinations as comb
from collections import deque
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def count(comb_restaurants, data):
    temp = 0
    q = deque(comb_restaurants)
    visit = [[0] * N for _ in range(N)]
    for i, j in comb_restaurants:
        temp += data[i][j]
        visit[i][j] = 1
    while q:
        r, c = q.popleft()
        if data[r][c] == 1:
            temp += visit[r][c] - 1
            if temp >= answer:
                return temp
        for i in range(4):
            nr = r + dy[i]
            nc = c + dx[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c] + 1
                    q.append((nr, nc))
    return temp



T = int(input())
for tc in range(1, T+1):
    answer = 400 * 100
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    restaurants = [(i, j) for j in range(N) for i in range(N) if data[i][j] > 1]
    for i in range(len(restaurants)):
        for comb_restaurants in list(comb(restaurants, i+1))[::-1]:
            answer = min(answer, count(comb_restaurants, data))
    print(f'#{tc} {answer}')

