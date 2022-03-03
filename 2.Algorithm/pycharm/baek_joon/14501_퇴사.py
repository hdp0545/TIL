N = int(input())
data = [map(int, input().split()) for _ in range(N)]
dp = [0 for _ in range(N+1)]
answer = 0
for i in range(N):
    t, p = data[i]
    answer = max(answer, dp[i])
    if i+t < N+1:
        dp[i+t] = max(dp[i+t], answer + p)
print(max(answer, dp[N]))

