answer = []
for tc in range(1, int(input())+1):
    W, H, N = map(int, input().split())
    lc = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N-1):
        dx, dy = lc[i][0] - lc[i+1][0], lc[i][1] - lc[i+1][1]
        result += max(abs(dx), abs(dy)) if dx * dy >= 0 else abs(dx) + abs(dy)
    answer.append(f'#{tc} {result}')
print('\n'.join(answer))
