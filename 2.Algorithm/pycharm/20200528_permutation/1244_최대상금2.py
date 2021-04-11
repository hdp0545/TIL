for C in range(1, int(input())+1):
    number, chance = input().split()
    n_list = [n for n in number]
    n_list = list(map(int, n_list))
    chance = int(chance)
    temp = [[] for _ in range(10)]
    for idx, n in enumerate(n_list):
        temp[n].append(idx)
    i = 0
    for n, idxs in enumerate(temp[::-1]):
        if len(idxs) <= chance:
            idxs.sort()
            target = sorted(n_list[i:i+len(idx)])
            for idx in idxs:
                n_list[idx] = target.pop()
    #
    # while i != cnt:
    #     my_max = my_max_idx = 0
    #     for j in range(len(n_list)-1, i-1, -1):
    #         if my_max < n_list[j]:
    #             my_max, my_max_idx = n_list[j], j
    #     if n_list[i] == my_max:
    #         i += 1
    #         cnt += 1
    #         if i == len(n_list):
    #             break
    #     else:
    #         n_list[my_max_idx] = n_list[i]
    #         n_list[i] = my_max
    #         if i > 0 and n_list[i - 1] == n_list[i]:
    #             cnt += 2
    #             i += 1
    #         i += 1
    # if (cnt - i) & 1 and len(n_list) == len(set(n_list)):
    #     n_list[-1], n_list[-2] = n_list[-2], n_list[-1]
    #     print('#{} {}'.format(C, ''.join(map(str, n_list))))
    # else:
    #     print('#{} {}'.format(C, ''.join(map(str, n_list))))
