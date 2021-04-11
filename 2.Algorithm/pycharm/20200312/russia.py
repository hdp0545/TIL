from itertools import combinations_with_replacement
color = ['W', 'B', 'R']


def my_count(cnt=0, j=-1):
    for i in range(3):
        for j in range(j+1, j+c_c[i]+1):
            cnt += flag[j].count(color[i])
    return cnt


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    counts = list(combinations_with_replacement([0, 1, 2], N-3))
    result = 0
    for C in counts:
        c_c = [1, 1, 1]
        for c in C:
            c_c[c] += 1
        temp = my_count()
        if result < temp:
            result = temp
    print(f'#{tc} {N*M - result}')

