T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for i in range(M):
        if i == 0:
            data = list(map(int, input().split()))
        else:
            target = list(map(int, input().split()))
            for idx, d in enumerate(data):
                if d > target[0]:
                    data[idx:0] = target
                    break
            else:
                data += target
    print('#', tc, sep='', end=' ')
    for i in range(-1, -11, -1):
        print(data[i], end=' ')
    print()