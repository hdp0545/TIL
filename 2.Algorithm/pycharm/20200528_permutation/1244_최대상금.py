for C in range(1, int(input())+1):
    number, cnt = input().split()
    n_list = [n for n in number]
    n_list = list(map(int, n_list))
    cnt = int(cnt)
    i = 0
    while i != cnt:
        my_max = my_max_idx = 0
        for j in range(len(n_list)-1, i-1, -1):
            if my_max < n_list[j]:
                my_max, my_max_idx = n_list[j], j
        if n_list[i] == my_max:
            i += 1
            cnt += 1
            if i == len(n_list):
                break
        else:
            n_list[my_max_idx] = n_list[i]
            n_list[i] = my_max
            if i > 0 and n_list[i - 1] == n_list[i]:
                cnt += 2
                i += 1
            i += 1
    if (cnt - i) & 1 and len(n_list) == len(set(n_list)):
        n_list[-1], n_list[-2] = n_list[-2], n_list[-1]
        print('#{} {}'.format(C, ''.join(map(str, n_list))))
    else:
        print('#{} {}'.format(C, ''.join(map(str, n_list))))
