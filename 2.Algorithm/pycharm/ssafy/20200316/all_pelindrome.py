for tc in range(1, int(input()) + 1):
    word = input()
    N = len(word)
    result = 'Exist'
    for i in range(N//2):
        if word[i] != '?' and word[N-i-1] != '?' and word[i] != word[N-i-1]:
            result = 'Not exist'
            break
    print(f'#{tc} {result}')