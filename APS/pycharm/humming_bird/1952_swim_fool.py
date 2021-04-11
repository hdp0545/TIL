def f(n, s):
    global r
    if n >= 12:
        r = min(r, s)

    else:
        f(n + 1, s + (day * monthplan[n]))
        f(n + 1, s + month)
        f(n + 3, s + month3)


T = int(input())
for t in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    monthplan = list(map(int, input().split()))
    r = year
    f(0, 0)
    print('#{} {}'.format(t, r))