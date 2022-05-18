T = int(input())
for test_case in range(1, T + 1):
    K, N, M = (map(int, input().split()))
    N_list = list(map(int, input().split()))
    dis = cnt = 0
    while dis < N - K:
        dis = dis + K
        if N_list[0] > dis:
            cnt = 0
            break
        while N_list != [] and N_list[0] <= dis:
            short = N_list.pop(0)
        dis = short
        cnt += 1
    print('#{} {}'.format(test_case, cnt))
