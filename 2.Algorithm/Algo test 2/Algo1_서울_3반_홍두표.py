def no_sudoku(r, c, value):
    for i in range(9):      # 가로 세로, value 있는지 판단
        if sudoku[r][i] == value:
            return True
        if sudoku[i][c] == value:
            return True
    sr, sc = (r // 3) * 3, (c // 3) * 3     # 정사각형의 좌상단 좌표 탐색
    for i in range(3):
        for j in range(3):
            if sudoku[sr+i][sc+j] == value: # 정사각형의 좌상단 부터 정사각형 모두 탐색
                return True
    sudoku[r][c] = value
    return False    # 모두 스도쿠가 된다면 False 출력


for tc in range(1, int(input())+1):
    # input 받기
    N = int(input())
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    moves = [list(map(int, input().split())) for _ in range(N)]
    result = 0  # 처음에 실패할 경우 0 출력
    for move in moves: # 명령수만큼 시뮬레이션 해보기
        r, c, value = move
        if no_sudoku(r, c, value):  # 스도쿠가 안되는지 판단하기
            break       # 안 된다면 break
        result += 1     # 성공시마다 횟수 증가
    print(f'#{tc} {result}')
5