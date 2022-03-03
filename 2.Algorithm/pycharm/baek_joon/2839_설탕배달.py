N = int(input())
DP = [5000]*5006
DP[3] = DP[5] = 1
for i in range(1, N-2):
    if DP[i] != 5000:
        DP[i+3] = min(DP[i+3], DP[i] + 1)
        DP[i+5] = min(DP[i+5], DP[i] + 1)
print(-1 if DP[N] == 5000 else DP[N])

