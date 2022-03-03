for _ in range(int(input())):
    d = (lambda x: int(x[1]) - int(x[0]))(input().split())
    i, cnt = 0, 0
    while d > 2*i - cnt:
        cnt += 1
        i += cnt
    i -= cnt
    r = (d - 2 * i) // cnt + int(bool((d - 2 * i) % cnt))
    print(2 * (cnt-1) + r)