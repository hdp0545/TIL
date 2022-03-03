T = int(input())
for tc in range(1, T+1):
    N = int(input())
    target = [0] + list(map(int, input().split()))
    cnt = 0
    temp = [0] * (N+1)
    for x in range(1, N+1):
        if target[x] != temp[x]:
            for x in range(x, N+1, x):
                if temp[x] == 0:
                    temp[x] = 1
                else:
                    temp[x] = 0
            cnt += 1
    print('#{} {}'.format(tc, cnt))

