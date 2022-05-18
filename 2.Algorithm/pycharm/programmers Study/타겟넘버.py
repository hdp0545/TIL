from itertools import product

def solution(numbers, target):
    answer = 0
    N = len(numbers)
    for bools in product([True, False], repeat=N):
        temp = 0
        for i in range(N):
            temp += numbers[i] if bools[i] else -numbers[i]
        if temp == target:
            answer += 1
    return answer

print(solution([1, 1, 1, 1, 1], 3))