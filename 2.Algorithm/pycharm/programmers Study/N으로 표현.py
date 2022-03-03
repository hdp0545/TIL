def cal(a, b):
    stack = set([])
    for i in a:
        for j in b:
            stack.add(i + j)
            stack.add(i * j)
            if i > j:
                stack.add(i - j)
                if j:
                    stack.add(i // j)
            else:
                stack.add(j - i)
                if i:
                    stack.add(j // i)
    return stack

def solution(N, number):
    answer = -1
    dp = [{N}, {N*11}, {N*111}, {N*1111}, {N*11111}, {N*111111}, {N*1111111}, {N*11111111}]
    for i in range(8):
        for k in range(i):
            n_set = cal(list(dp[k]), list(dp[i-1-k]))
            dp[i] = dp[i] | n_set
            if k <= i - 1 -k:
                break
        if number in dp[i]:
            return i + 1
    return answer

print(solution(2, 24))