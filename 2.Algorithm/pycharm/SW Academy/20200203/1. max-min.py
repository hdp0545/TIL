T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    min_n = max_n = N_list[0]
    for n in range(1, N):
        if N_list[n] > max_n:
            max_n = N_list[n]
        if N_list[n] < min_n:
            min_n = N_list[n]

    print('#{} {}'.format(test_case, max_n - min_n))



    name = ""