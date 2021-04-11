f = lambda x: (int(x) - 1) // 2
for tc in range(1, int(input()) + 1):
    N = int(input())
    passage = [0] * 200
    for _ in range(N):
        a, b = map(f, input().split())
        if a > b:
            a, b = b, a
        for i in range(a, b + 1):
            passage[i] += 1
    print('#%d %d' % (tc, max(passage)))
