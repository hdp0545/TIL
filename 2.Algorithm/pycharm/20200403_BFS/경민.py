def move(enemy):
    result = []
    for i in enemy:
        if i[0]+1 < N:
            result.append((i[0]+1,i[1]))
    return result


def comb(M):
    cases = []
    for i in range(1<<M):
        c = []
        for j in range(M):
            if i&1:
                c.append(j)
            i = i//2
            if len(c)>3: break
        if len(c)==3:
            cases.append(tuple(c))
    return cases


def attack(a, enemy):
    global cnt
    result = set()
    for i in a:
        temp = sorted(enemy,key = lambda j: (N-j[0]+abs(i-j[1]),j[1]))
        if N-temp[0][0]+abs(i-temp[0][1]) <= D:
            result.add(temp[0])
    new_enemy = [i for i in enemy if i not in result]
    cnt += len(enemy)-len(new_enemy)
    return new_enemy


N,M,D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
enemy = [(i,j) for j in range(M) for i in range(N) if arr[i][j]]
mx = 0
for c in comb(M):
    cnt = 0
    enm = enemy[:]
    while enm:
        enm = attack(c,enm)
        enm = move(enm)
    if mx < cnt:
        mx = cnt
print(mx)