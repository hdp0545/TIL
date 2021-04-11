T = int(input())
for test_case in range(1, T+1):
    N, M = (map(int, input().split()))
    N_list = list(map(int, input().split()))
    for idx in range(N-M+1):
        sample = 0
        for j in range(M):
            sample += N_list[idx+j]
        if idx == 0:
            max_n = min_n = sample
        if sample > max_n:
            max_n = sample
        if sample < min_n:
            min_n = sample
    print('#{} {}'.format(test_case, max_n - min_n))

    #sum을 하나하나 계산하지 말고 계산된 초기값에서 계산하자.
