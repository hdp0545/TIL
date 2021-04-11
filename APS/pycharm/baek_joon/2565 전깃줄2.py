N = int(input())
raw = [list(map(int, input().split())) for _ in range(N)]
raw.sort(key=lambda x: x[0])
arr = [0] * N
for i in range(N):
    for j in range(i):
        if raw[i][1] > raw[j][1]:
            arr[i] = max(arr[i], arr[j] + 1)
print(N - max(arr) - 1)


