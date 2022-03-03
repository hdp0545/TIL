def backtrack(k=0, r=1):
    c = []
    global max_p
    if r <= max_p:
        return
    if k == N:
        max_p = r
        return
    else:
        for i in range(N):
            if check[i]:
                c.append(i)
        for i in range(N-k):
            check[c[i]] = False
            backtrack(k+1, r * arr[k][c[i]])
            check[c[i]] = True


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    check = [True] * N
    max_p = 0
    backtrack()
    print('#%d %.6f' % (tc, max_p * 100))