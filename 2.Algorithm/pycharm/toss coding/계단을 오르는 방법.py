def solution(numOfStairs):
    dp = [0] * numOfStairs
    dp[0] = 1
    if numOfStairs > 1:
        dp[1] = 2
    if numOfStairs > 2:
        dp[2] = 4
    if numOfStairs > 3:
        for i in range(3, numOfStairs):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[-1]

print(solution(70))