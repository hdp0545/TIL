def f(n, k, r, op1, op2, op3, op4):
    global minV, maxV
    if n == k:
        if maxV < r:
            maxV = r
        if minV > r:
            minV = r
    else:
        if op1:
            f(n+1, k, r + numbers[n], op1-1, op2, op3, op4)
        if op2:
            f(n+1, k, r - numbers[n], op1, op2-1, op3, op4)
        if op3:
            f(n+1, k, r * numbers[n], op1, op2, op3-1, op4)
        if op4:
            f(n+1, k, int(r/numbers[n]), op1, op2, op3, op4-1)


for test_case in range(1, int(input()) + 1):
    N = int(input())
    op1, op2, op3, op4 = map(int, input().split())
    numbers = list(map(int, input().split()))
    minV = 10000000000
    maxV = -10000000000
    f(1, N, numbers[0], op1, op2, op3, op4)
    print('#{} {}'.format(test_case, maxV - minV))
