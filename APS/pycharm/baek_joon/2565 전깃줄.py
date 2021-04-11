N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
raw.sort(key=lambda x: x[0])
check = [[] for _ in range(N)]
for i in range(N-1):
    end = raw[i][1]
    for j in range(i + 1, N):
        if raw[j][1] < end:
            check[i].append(j)
            check[j].append(i)
print(raw)
print(check)
cnt = 0
while True:
    max_nodes = 0
    flag = False
    for i in range(N):
        if len(check[i]) > max_nodes:
            max_nodes = len(check[i])
            max_idx = i
            flag = True
    if not flag:
        break
    for i in check[max_idx]:
        check[i].remove(max_idx)
    check[max_idx] = []
    cnt += 1
print(cnt)
