T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))
    for _ in range(M):
        com = input()
        if com[0] == 'I':
            C, I, D = com.split()
            data[int(I):int(I)] = [int(D)]
        elif com[0] == 'D':
            C, I = com.split()
            del data[int(I)]
        elif com[0] == 'C':
            C, I, D = com.split()
            data[int(I)] = int(D)
    if 0 <= L < len(data):
        result = data[L]
    else:
        result = -1
    print('#{} {}'.format(tc, result))
