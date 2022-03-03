for test_case in range(1, int(input())+1):
    N = int(input())
    data = input().split()
    print(data)
    end = ['.', '?', '!']
    i = cnt = flag = 0
    result = [0]*N
    while i < len(data):
        j = 0
        if data[i][len(data[i]) - 1] in end:
            flag = 1
        if ord('A') <= ord(data[i][0]) <= ord('Z'):
            j = 1
            while j < len(data[i]) - flag:
                if not ord('a') <= ord(data[i][j]) <= ord('z') :
                    break
                j += 1
            else:
                result[cnt] += 1
        if flag == 1:
            flag = 0
            cnt += 1
        i += 1
    print('#{} {}'.format(test_case, ' '.join(map(str, result))))