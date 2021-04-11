result = [0]
T = int(input())
for _ in range(T):
    N = int(input())
    N_list = list(map(int, input().split()))
    max_score = sum(N_list)
    temp = 0
    n = N
    cnt = 1
    score_list = [0] * (max_score+1)
    while not score_list[-1]:
        for i in range(n):
            score_list[temp + N_list[i]] = 1
            if i == n-1:
                temp += N_list[i]
        n -= 1
    for j in range(max_score+1):
        if score_list[j]:
            cnt += 1
    result.append(cnt)
for t in range(1, T+1):
    print('#{} {}'.format(t, result[t]))