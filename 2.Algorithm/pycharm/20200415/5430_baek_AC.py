import sys
# from collections import deque
sys.stdin = open("test.txt",'r')
T = int(input())
for t in range(1,T+1):
    working = list(input())
    n = int(input())
    k = 0
    d = 1
    data = list(input()[1:-1].split(','))
    for w in working:
        if w == 'R':
            d *= -1
            if d == -1:
                k, n = n-1, k-1
            else:
                k, n = n+1, k+1
        else:
            k += d
            if (k > n and d == 1) or (k < n and d == -1):
                print('error')
                break
    else:
        result = [data[i] for i in range(k, n, d)]
        print('[', end='')
        print(','.join(map(str, result)), end='')
        print(']')