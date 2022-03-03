N = int(input())
DP = [[0, 0, 0] for _ in range(N + 1)]
colors = [tuple(map(int, input().split())) for _ in range(N)]
DP[1] = list(colors[0])
for i in range(1, N):
    for c in range(3):
        temp = []
        for j in range(3):
            if j != c:
                temp.append(DP[i][j] + colors[i][c])
        DP[i + 1][c] = min(temp)
print(min(DP[N]))
