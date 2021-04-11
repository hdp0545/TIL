N = int(input())
win_lose = {}
winner = {}
for _ in range(N*(N-1)):
    temp = list(input().split())
    if win_lose.get(temp[0], False):
        win_lose[temp[0]][0] += int(temp[1])
        win_lose[temp[0]][1] += int(temp[3])
    else:
        win_lose[temp[0]] = [int(temp[1]), int(temp[3]), 0]
    if win_lose.get(temp[2], False):
        win_lose[temp[2]][0] += int(temp[3])
        win_lose[temp[2]][1] += int(temp[1])
    else:
        win_lose[temp[2]] = [int(temp[3]), int(temp[1]), 0]
    if temp[1] > temp[3]:
        win_lose[temp[0]][2] += 1
    else:
        win_lose[temp[2]][2] += 1
result = sorted(win_lose.items())
result1 = sorted(result, key=lambda x: x[1][0] - x[1][1], reverse=True)
result2 = sorted(result1, key=lambda x: x[1][2], reverse=True)
for key, value in result2:
    print(f'{key} {value[2]} {value[0] - value[1]}')
