for test_case in range(1, int(input())+1):
    P, Q, R, S, W = (map(int, input().split()))
    P_fee = W * P
    if W <= R:
        Q_fee = Q
    else:
        Q_fee = Q + ((W - R) * S)

    if P_fee < Q_fee:
        result = P_fee
    else:
        result = Q_fee

    print('#{} {}'.format(test_case, result))