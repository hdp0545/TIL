# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    temp = [0 for _ in range(N)]
    answer = 0
    t = 0
    for a in A:
        temp[a-1] += 1
    for n in temp:
        t += n - 1
        answer += abs(t)
        if answer > 1000000000:
            return -1
    return answer

print(solution([1, 1, 1, 4]))
