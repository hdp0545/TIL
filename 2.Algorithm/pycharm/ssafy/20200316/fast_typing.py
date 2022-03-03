for test_case in range(1, int(input())+1):
    target, word = input().split()
    l_t, l_w = len(target), len(word)
    i = 0
    result = l_t
    jump = [l_w for _ in range(128)]
    for idx_w in range(l_w - 1):
        jump[ord(word[idx_w])] = l_w - 1 - idx_w
    while i < (l_t - l_w + 1):
        j = l_w - 1
        k = i + l_w - 1
        while j >= 0 and word[j] == target[k]:
            j -= 1
            k -= 1
        if j == -1:
            i += l_w
            result -= l_w - 1
        else:
            i += jump[ord(target[i + l_w - 1])]
    else:
        print('#{} {}'.format(test_case, result))