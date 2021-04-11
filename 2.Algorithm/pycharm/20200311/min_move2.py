def cross(i1, j1, i2, j2):
    global count
    if i2 > i1 and j2 > j1:
        if i2 >= j2:
            count += j2 - j1
            i1 += j2 - j1
            j1 = j2
        else:
            count += i2 - i1
            j1 += i2 - i1
            i1 = i2
    elif i1 > i2 and j1 > j2:
        if i1 >= j1:
            count += j1 - j2
            i1 -= j1 - j2
            j1 = j2
        else:
            count += i1 - i2
            j1 -= i1 - i2
            i1 = i2
    if i1 > i2:
        count += i1 - i2
        i1 = i2
    elif i1 < i2:
        count += i2 - i1
        i1 = i2
    if j1 > j2:
        count += j1 - j2
        j1 = j2
    elif j1 < j2:
        count += j2 - j1
        j1 = j2
T = int(input())
for case in range(1, T + 1):
    W, H, N = map(int, input().split())
    jwapyo = [list(map(int, input().split())) for _ in range (N)]
    count = 0
    for i in range(N-1):
        cross(jwapyo[i][0], jwapyo[i][1], jwapyo[i+1][0], jwapyo[i+1][1])
    print('#{} {}'.format(case, count))