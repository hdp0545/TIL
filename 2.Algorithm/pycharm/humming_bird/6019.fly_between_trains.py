T = int(input())
rs = []
for _ in range(T):
    D, A, B, F = map(int, input().split())
    rs += [D / (A+B) * F]
for t in range(T):
    print(f'#{t+1} {rs[t]}')