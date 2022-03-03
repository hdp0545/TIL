tc = int(input())
for t in range(1, tc + 1):
    # 2차원 배열에 문자 넣기
    ar = [['']*15 for _ in range(5)]

    for i in range(5):
        for j, w in enumerate(input()):
            ar[i][j] = w

    result = ''
    for i in range(15):
        for j in range(5):
            if len(ar[j]) - 1 >= i:
                result += ar[j][i]

    print('#{} {}'.format(t, result))