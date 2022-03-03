def press(x, y, target):
    l, r, b, t = target
    if l <= x <= r and b <= y <= t:
        return True
    return False

N, M = map(int, input().split())
my_dict = {}
for i in range(N):
    my_dict[i+1] = 0
buttons = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    for i in range(N-1, -1, -1):
        if press(x, y, buttons[i]):
            my_dict[i+1] += 1
            break

for i in range(N):
    print(f'Button #{i+1}: {my_dict[i+1]}')