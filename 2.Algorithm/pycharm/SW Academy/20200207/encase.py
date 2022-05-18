#인풋 형태가 N X N 형태로 들어올때
N = int(input())
a = [[0]*(N+2)]
a += [[0]+list(map(int, input().split())) + [0] for _ in range(N)]
a += [[0]*(N+2)]
print(a)

