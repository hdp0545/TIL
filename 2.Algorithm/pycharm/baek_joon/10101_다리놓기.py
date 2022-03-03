N = int(input())
answers = []
for _ in range(N):
    a, b = map(int, input().split())
    answer = 1
    div = 1
    for i in range(a):
        answer *= (b - i)
        div *= (i + 1)
    answer //= div
    print(answer)
