for test_case in range(1,int(input())+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    result = -1
    for i in range(N-1):
        for j in range(i+1, N):
            words = N_list[i] * N_list[j]
            if words > result:
                word = str(words)
                l = len(word)
                for idx in range(l-1):
                    if int(word[idx]) > int(word[idx+1]):
                        break
                else:
                    result = words
    print('#{} {}'.format(test_case, result))
