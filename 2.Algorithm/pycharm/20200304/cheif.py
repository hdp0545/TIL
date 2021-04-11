def f(k=-1, n=0, st=''):
    if n == N//2:
        global result
        check = list(map(int, st.split()))
        A = 0
        B = 0
        for i in range(N):
            if i in check:
                for j in range(N):
                    if j in check:
                        A += arr[i][j]
            else:
                for j in range(N):
                    if j not in check:
                        B += arr[i][j]
        if result > abs(A-B):
            result = abs(A-B)
        return
    for i in range(k+1, N):
        f(i, n+1, st + ' ' + str(i))


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 40000
    f()
    print('#%d %d'%(tc, result))