from itertools import permutations as pp

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 1000
    for i in pp(range(1, N)):
        start = battery = 0
        for j in i:
             battery += arr[start][j]
             start = j
        battery += arr[start][0]
        if battery < result:
            result = battery
    print('#{} {}'.format(tc, result))