dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * (N + 2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 2)] # 패딩 하기

    # DFS사용 및 결과값, 넓이 초기화
    stack = []
    result = 0
    area = 0

    # 모든 케이스 확인하기
    for i in range(1, N+1):
        for j in range(1, N+1):

            # 매트릭스 + 비짓 이 값이 있으면 시작 합치기
            if matrix[i][j]:
                # c는 매장량
                c = matrix[i][j]
                matrix[i][j] = 0
                # cnt는 땅 갯수
                cnt = 0
                stack.append((i, j))
                # DFS 코드
                while stack:
                    ni, nj = stack.pop()
                    cnt += 1
                    # 8방향 탐색하기
                    for k in range(8):
                        # 자신의 매장량과 같은 매장량 탐색후 스택에 넣기
                        if matrix[ni + dy[k]][nj + dx[k]] == c:
                            stack.append((ni + dy[k], nj + dx[k]))
                            # 넣은 땅은 비짓을 0으로 만들기
                            matrix[ni + dy[k]][nj + dx[k]] = 0
                # 결과값을 전체 매장량중의 최대값을 결과값으로 바꾸기
                if result < c * cnt:
                    result = c * cnt
                    area = cnt
    print('#{} {} {}'.format(tc, result, area))


