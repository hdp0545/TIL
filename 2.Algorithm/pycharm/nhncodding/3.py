N, M = map(int, input().split())
collors = list(input().split())
my_dict = {}
for i in range(N):
    my_dict[collors] = 0
rundry = [list(input().split()) for _ in range(M)]

rundry.sort(key=lambda x: int(x[0]))
rundry.sort(key=lambda x:x[1])

flag = False
time = 0
collor = collors[0]
for i in range(M):
    if collor == rundry[1]:
        int(rundry[0])
    else:
        my_dict[collor] += time