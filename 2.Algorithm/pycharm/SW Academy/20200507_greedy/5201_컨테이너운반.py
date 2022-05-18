for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    result = 0
    i = 0
    trucks.sort(reverse=True)
    weights.sort(reverse=True)
    for truck in trucks:
        for idx in range(i, N):
            if truck >= weights[idx]:
                result += weights[idx]
                i = idx + 1
                break
        else:
            i = N
    print(f'#{tc} {result}')