gan_sun = list(map(int, input().split(', ')))
Ng = len(gan_sun)//2
Ns = max(gan_sun)
in_list = [[] for _ in range(Ns + 1)]
for i in range(Ng):
    in_list[gan_sun[2*i]].append(gan_sun[2*i+1])
    in_list[gan_sun[2*i+1]].append(gan_sun[2*i])

print(in_list)

visited = [0]*(Ns+1)
stack = []
result = []
v = 1
stack.append(v)
while stack:
    if visited[v] == 0:
        visited[v] = 1
        #stack.append(v)
        result.append(v)
    for w in in_list[v]:
        if visited[w] == 0:
            #여기에 추가
            stack.append(v)
            v = w
            break
    else:
        v = stack.pop(-1)
print(result)
