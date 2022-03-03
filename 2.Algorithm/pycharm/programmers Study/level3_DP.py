def solution(n, money):
    dp = [0 for i in range(n+1)]
    money.sort(reverse=True)
    for m in money:
        dp[m] = 1
        for i in range(1, n+1):
            if i % m == 0:
                dp[i] += dp[i-m]

    return dp[n]



print(solution(10, [1, 2, 5]))