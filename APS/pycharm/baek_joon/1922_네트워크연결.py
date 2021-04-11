N = int(input())
M = int(input())
datas = [list(map(int, input().split())) for _ in range(M)]
graph = [0] * (N + 1)
datas.sort(key=lambda x: x[2], reverse=True)
result = 0
print(datas)
for data in datas:
    a, b, c = data
    graph[a] += 1
    graph[b] += 1
    result += c
flag = True
temp = 0
for data in datas:
    a, b, c = data
    print(graph)
    if flag and (graph[a] == 2 and graph[b] == 2):
        temp = c
        flag = False
        print(data)
    if graph[a] > 2 and graph[b] > 2:
        graph[a] -= 1
        graph[b] -= 1
        result -= c
        print(graph)
        print(result)

print(result)