def mymax(list):
    length = len(list)
    max = list[0]
    cnt = 0
    for i in range(1, length):
        if max <= list[i]:
            max = list[i]
            cnt = i
    return cnt

for test_case in range(1, int(input())+1):
    N = input()
    N_list = list(map(int, input().split()))
    cnt = [0]*101
    for score in N_list:
        cnt[score] += 1
    print('#{} {}'.format(N, mymax(cnt)))