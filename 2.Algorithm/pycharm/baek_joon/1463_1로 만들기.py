N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):
    temp = []
    if i % 3 == 0:
        n = dp[i//3] + 1
        temp.append(n)
    if i % 2 == 0:
        n = dp[i//2] + 1
        temp.append(n)
    n = dp[i-1] + 1
    temp.append(n)
    dp[i] = min(temp)
print(dp[N])
