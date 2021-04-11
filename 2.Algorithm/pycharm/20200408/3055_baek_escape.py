import sys
sys.stdin = open("test.txt", "r")

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def water_spread():
    while water_stack:
        y, x = water_stack.pop()
        for i in range(4):
            X, Y = dx[i] + x, dy[i] + y
            if 0<=X<=C-1 and 0<=Y<=R-1: # 경계조건
                if Map[Y][X] !='D' and Map[Y][X] !='X' and Map[Y][X] != '*': # 비버와 돌이 아니면 확장
                    Map[Y][X] = '*'
                    new_water_stack.append([Y,X])

def gosum():

    while stack:
        b, a = stack.pop()
        for j in range(4):
            A, B = dx[j] + a, dy[j] + b
            if 0 <= A <= C - 1 and 0 <= B <= R - 1:  # 경계조건
                if Map[B][A] == 'D':
                    return V[b][a]
                elif Map[B][A] != '*' and Map[B][A] != 'X' and V[B][A] == 0:  # 비버와 돌이 아니면 확장
                    new_gosum_stack.append([B, A])
                    V[B][A] = V[b][a] + 1
    return False


R, C = list(map(int,input().split()))
Map = [list(map(str, input())) for _ in range(R)]
# print(Map)

V = [[0]*C for _ in range(R)] # 방문한곳이랑 물있는곳을 1로 처리
t, u = 0, 0
water_stack = []
for r in range(R):
    for c in range(C):
        if Map[r][c] == 'S':
            t, u = r, c
        if Map[r][c] == '*':
            water_stack.append([r,c])

stack = [[t,u]]
V[t][u] = 1
new_water_stack = []
new_gosum_stack = []

while True:
    water_spread()
    result = gosum()
    if result:
        print(result)
        break
    if not new_gosum_stack:
        print('KAKTUS')
        break
    stack = new_gosum_stack[:]
    new_gosum_stack = []
    water_stack = new_water_stack[:]
    new_water_stack = []