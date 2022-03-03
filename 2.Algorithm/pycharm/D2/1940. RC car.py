for test_case in range(1, int(input())+1):
    N = int(input())
    Vs = [list(map(int, input().split())) for i in range(N)]
    V = 0
    result = 0
    for i in Vs:
        if i[0] == 1:
            V += i[1]
        if i[0] == 2:
            V -= i[1]
        if V < 0 :
            V = 0
        result += V

    print('#{} {}'.format(test_case, result))