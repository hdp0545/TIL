T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    for n in range(N): # A에 있는 데이터를 B에 옮겨서 계산
        B = [0]*10
        for i in range(10):
            if A[i]:  # A[i]가 있는 경우 시작
                if abs(A[i]) >= 10:  # 절대값이 10 이상인 경우
                    if i == 0:  # 양 끝값인 경우 자기 이동하지 못하고 부호가 바뀐 채, B에 저장
                        B[i] += abs(A[i]) // 2
                        B[i+1] += abs(A[i]) // 2
                    elif i == 9:
                        B[i] += -abs(A[i]) // 2
                        B[i-1] += -abs(A[i]) // 2
                    else:  # 양 끝값이 아닌경우 양 쪽으로 나뉘어져 양수는 오른쪽으로 음수는 왼쪽으로 이동
                        B[i+1] += abs(A[i]) // 2
                        B[i-1] += -abs(A[i]) // 2
                else:  # 10보다 작은 경우
                    if A[i] > 0:   # 양수인 경우
                        if i == 9:  # 오른쪽 끝값인 경우 부호만 바뀌고 자기자리에 저장
                            B[i] += -A[i]
                        else:  # 아니면 A[i] 값이 오른쪽으로 이동하여 저장
                            B[i+1] += A[i]
                    if A[i] < 0:  # 음수인 경우
                        if i == 0:  # 왼쪽 끝값인 경우 부호만 바뀌고 자기자리에 저장
                            B[i] += -A[i]
                        else:  # 아니면 왼쪽 이동
                            B[i-1] += A[i]
        A = B[:]  #바뀐 케이스를 A로 저장
    print("#{} {}".format(tc, ' '.join(map(str, A))))
