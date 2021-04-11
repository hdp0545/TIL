T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    data = input()
    data += data[:N//4]
    numbers = sorted(list(map(lambda x: int(x, 16), set([data[i:i + N//4] for i in range(N)]))), reverse=True)
    print('#{} {}'.format(t, numbers[K-1]))
