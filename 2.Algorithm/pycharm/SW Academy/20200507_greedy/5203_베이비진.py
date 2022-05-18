def run_a(list_a):
    i = 0
    while i < 8:
        if list_a[i] and list_a[i+1] and list_a[i+2]:
            return True
        i += 1
    return False


def winner():
    player1 = [0] * 10
    player2 = [0] * 10
    for i in range(6):
        player1[data[2 * i]] += 1
        player2[data[2 * i + 1]] += 1
        if player1[data[2 * i]] == 3:
            return 1
        else:
            if run_a(player1):
                return 1
        if player2[data[2 * i + 1]] == 3:
            return 2
        else:
            if run_a(player2):
                return 2
    return 0


for tc in range(1, int(input())+1):
    data = list(map(int, input().split()))
    print('#{} {}'.format(tc, winner()))



