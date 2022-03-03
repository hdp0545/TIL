from collections import deque

for t in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_list = [0] * 1000001
    queue = deque()
    queue.append(N)
    while True:
        num = queue.popleft()
        if num == M:
            break
        num_cnt = num_list[num]
        for i in range(4):
            a = num
            if i == 0:
                a += 1
            elif i == 1:
                a -= 1
            elif i == 2:
                a *= 2
            else:
                a -= 10
            if 0 <= a <= 1000000:
                if not num_list[a]:
                    num_list[a] = num_cnt + 1
                    queue.append(a)

    print('#{} {}'.format(t, num_list[M]))