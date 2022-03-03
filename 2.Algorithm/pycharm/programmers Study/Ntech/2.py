def solution(N):
    answer = 0
    test_N = N // 2
    for i in range(test_N + 1):
        if i == 0:
            answer += 1
        else:
            temp = 1
            for j in range(i):
                temp *= N - i - j
            for j in range(2, i+1):
                temp /= j
            answer += temp



    return int(answer)

print(solution(7))