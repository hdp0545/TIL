N = int(input())
data = [input() for _ in range(N)]
answer = list(data[0])
for i in range(1, N):
    for j in range(len(answer)):
        if answer[j] != '?' and answer[j] != data[i][j]:
            answer[j] = '?'
print(''.join(answer))