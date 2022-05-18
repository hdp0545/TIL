for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    target = list(map(int, input().split()))
    result = 0
    for t in target:
        l = 0
        r = N - 1
        flag = 0
        while l <= r:
            m = (l + r) // 2
            if A[m] == t:
                result += 1
                break
            elif A[m] < t and (flag == 0 or flag == 1):
                l = m + 1
                flag = 2
            elif A[m] > t and (flag == 0 or flag == 2):
                r = m - 1
                flag = 1
            else:
                break
    print(f'#{tc} {result}')