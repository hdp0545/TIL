def test(numbers):
    for i in range(9):
        for j in range(1, 10):
            if j not in numbers[i]:
                return 0
    else:
        return 1


def square_zip(numbers):
    new_matrix = [[numbers[(i // 3) * 3 + (j // 3)][(i % 3) * 3 + (j % 3)] for j in range(9)] for i in range(9)]
    return new_matrix


T = int(input())
for test_case in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    result = test(square_zip(matrix))
    if result == 1:
        result = test(matrix)
    if result == 1:
        result = test(list(map(list, zip(*matrix))))

    print('#{} {}'.format(test_case, result))