for test_case in range(1, int(input())+1):
    N = int(input())
    Nasa = list(map(int, input().split()))
    female = [Nasa[2*i + 1] for i in range(N)]
    male = [Nasa[2 * j] for j in range(N)]
    cnt = 0
    a, b = male[0], female[0]
    c = [str(a), str(b)]
    while b in male:
        a, b = male[male.index(b)], female[male.index(b)]
        c.extend([str(a), str(b)])
    a, b = male[0], female[0]
    while a in female:
        a, b = male[female.index(a)], female[female.index(a)]
        c.insert(0, str(b))
        c.insert(0, str(a))

    print('#{} {}'.format(test_case, ' '.join(c)))