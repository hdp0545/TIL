L, W, H = map(int, input().split())
n = int(input())
cubes = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    cubes[i][0] = 2 ** cubes[i][0]
cubes.sort(key=lambda x: x[0], reverse=True)
V = [0, 0, 0]
for i in range(n):
    if cubes[i][0] <= min(L, W, H):
        while cubes[i][1]:

            

            
