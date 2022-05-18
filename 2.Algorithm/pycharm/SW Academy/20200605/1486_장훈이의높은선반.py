T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    ki = list(map(int, input().split()))
    t = 0
    result = sum(ki)
    for i in range(1 << N):
        S = 0
        for j in range(N):
            if i & (1 << j):
                S += ki[j]
        if B <= S < result:
            result = S
    print(f'#{tc} {result - B}')