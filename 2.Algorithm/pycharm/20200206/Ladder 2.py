def my_min(list):
    min = list[0]
    for a in range(len(list)):
        if list[a] <= min:
            min = list[a]
            idx = a
    return idx

import sys
sys.stdin = open('input_ladder.txt', 'r')

for _ in range(10):
    test_case = int(input())
    matrix = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    start_point = [s for s in range(102) if matrix[0][s] == 1]    

    result = []
    for n in range(len(start_point)):
        length = 0
        idx = n
        for cnt in range(100):
            if matrix[cnt][start_point[idx]+1] == 1:
                length += start_point[idx + 1] - start_point[idx]
                idx += 1
            elif matrix[cnt][start_point[idx]-1] == 1:
                length += start_point[idx] - start_point[idx - 1]
                idx -= 1
        result.append(length)

    print('#{} {}'.format(test_case, start_point[my_min(result)] - 1))


