# 디피[i]= max(한칸 넘기고 두개 마시기 경우(디피[i-3] + 와인[i-1] +와인[i],  한칸 건너고 한개 마시기 경우(디피[i-2] + 와인[i]), 두번 연속으로 안마시기 (디피[i-1]))
N = int(input())
wine = [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
result = 0
for i in range(N):
    if i == 0:
        dp[i + 1] = wine[i]
    elif i == 1:
        dp[2] = dp[1] + wine[i]
    else:
        dp[i+1] = max(dp[i-2] + wine[i-1] + wine[i], dp[i-1] + wine[i], dp[i])
print(dp[-1])
