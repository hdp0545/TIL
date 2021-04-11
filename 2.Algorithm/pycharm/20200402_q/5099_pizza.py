for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    oven = [[0, 0]] * N     # 빈 공간의 오븐을 준비
    front = 0   # 내가 보는 방향(입구 방향)
    pizza = list(map(int, input().split())) + [2**20] * N
    for idx, ci in enumerate(pizza):    # pizza에 번호를 매기기
        while oven[front][1]:   # 오븐에 빈공간이 생길 때 까지 대기
            oven[front][1] //= 2    # 치즈 녹이기
            if oven[front][1] == 0:     # 치즈가 다 녹았다면
                result = oven[front][0]     # 피자 번호 체크하고 빼기
                break
            front = (front + 1) % N     # 피자 돌리기
        oven[front] = [idx + 1, ci]     # 오븐에 피자 넣기
        front = (front + 1) % N         # 피자 돌리기
    print('#{} {}'.format(tc, result))