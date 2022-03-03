from itertools import combinations as comb
from copy import deepcopy as deep

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def spread(gstack, rstack):
    global garden, cnt, gtemp, rtemp
    while gstack:
        i, j = gstack.pop()
        garden[i][j] = 0
        for k in range(4):
            ni, nj = i + dy[k], j + dx[k]
            if garden[ni][nj] == 1 or garden[ni][nj] == 2:
                garden[ni][nj] = 3
                gtemp.append((ni, nj))
    if not gtemp:
        return False

    while rstack:
        i, j = rstack.pop()
        garden[i][j] = 0
        for k in range(4):
            ni, nj = i + dy[k], j + dx[k]
            if garden[ni][nj] == 1 or garden[ni][nj] == 2:
                rtemp.append((ni, nj))
            if garden[ni][nj] == 3:
                cnt += 1
                garden[ni][nj] = 0
                del gtemp[gtemp.index((ni, nj))]
    if not rtemp:
        return False
    return True


N, M, G, R = map(int, input().split())
# 패딩하기
sample = [[0] * (M + 2)]
sample += [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
sample += [[0] * (M + 2)]
result = 0

# n에 씨앗을 심을 수 있는 장소 저장하기
n = [(i, j) for j in range(1, M + 1) for i in range(1, N + 1) if sample[i][j] == 2]

# 이중 조합 리스트 만들기
C = []
for i in comb(n, G):
    nn = n[:]
    for j in i:
        del nn[nn.index(j)]
    for k in comb(nn, R):
        C.append(i + k)

for c in C:
    cnt = 0
    gstack = []
    rstack = []
    garden = deep(sample)
    for i in range(G):
        gi, gj = c[i]
        garden[gi][gj] = 0
        gstack.append((gi, gj))
    for i in range(G, G + R):
        ri, rj = c[i]
        garden[ri][rj] = 0
        rstack.append((ri, rj))
    while True:
        gtemp = []
        rtemp = []
        if not spread(gstack, rstack):
            break
        gstack = gtemp
        rstack = rtemp
    if cnt > result:
        result = cnt
print(result)
