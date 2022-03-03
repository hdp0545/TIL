def solution(money):
    N = len(money)
    if N == 3:
        answer = max(money)
    else:
        money1 = money[1:]
        money2 = money[:N-1]
        for i in range(1, N-1):
            if i == 1:
                money1[i] = max(money1[i - 1], money1[i])
                money2[i] = max(money2[i - 1], money2[i])
            else:
                money1[i] = max(money1[i-1], money1[i] + money1[i-2])
                money2[i] = max(money2[i-1], money2[i] + money2[i-2])
        answer = max(money1[-1], money2[-1])
    return answer

print(solution([3000,2,100, 2999, 5]))