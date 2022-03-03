T = int(input())
for test_case in range(1, T+1):
    croak = 'croak'
    croaks = list(input())
    result = 0
    while croaks:
        i = j = 0
        while i <= len(croaks) - 1:
            if croaks[i] == croak[j % 5]:
                del croaks[i]
                j += 1
            else:
                i += 1
        if j % 5 or j == 0:
            result = -1
            break
        else:
            result += 1
    print('#{} {}'.format(test_case, result))


