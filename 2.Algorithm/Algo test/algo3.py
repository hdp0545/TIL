import sys
sys.stdin = open('input.txt', 'r')


def pandan(si, ei, sj, ej, target):
    for i in range(si, ei):
        for j in range(sj, ej):
            if matrix[i][j] == abs(target-1): # 타겟이 0이라면 반대로 1
                return False
    return True


def f(si, ei, sj, ej):
    # 전체가 0인지 판단
    if pandan(si, ei, sj, ej, 0):
        return '0'
    # 전체가 1인지 판단
    if pandan(si, ei, sj, ej, 1):
        return '1'
    # 범위를 4분할하여 재귀로 넣기
    a = f(si, (si+ei) // 2, sj, (sj+ej) // 2)
    b = f(si, (si+ei) // 2, (sj + ej) // 2, ej)
    c = f((si + ei) // 2, ei, sj, (sj + ej) // 2)
    d = f((si + ei) // 2, ei, (sj + ej) // 2, ej)
    # 그 값을 리턴
    return 'x{}{}{}{}'.format(a, b, c, d)


matrix = [list(map(int, input())) for _ in range(16)]
N = len(matrix)
print(f(0, N, 0, N))

#xx1110x1x100011xxx11000111x1x00111010