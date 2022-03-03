for t in range(1, int(input())+1):
    N = int(input())
    status = [0] * 5000
    for _ in range(N):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi + 1):
            status[i-1] += 1
    result = [status[int(input())-1] for _ in range(int(input()))]
    print('#{} {}'.format(t, ' '.join(map(str, result))))