T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = input()
    cards_cnt = [0] * 10

    for card in cards:
        cards_cnt[int(card)] += 1

    cnt = cards_cnt[0]
    value = 0

    for i in range(1, 10):
        if cards_cnt[i] >= cnt:
            cnt = cards_cnt[i]
            value = i

    print('#{} {} {}'.format(test_case, value, cnt))
