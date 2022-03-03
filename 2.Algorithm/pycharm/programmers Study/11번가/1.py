def solution(S):
    # write your code in Python 3.6
    answer = 0
    a_num = 0
    for s in S:
        if s == 'a':
            a_num += 1
            if a_num >= 3:
                return -1
        else:
            if a_num == 0:
                answer += 2
            elif a_num == 1:
                answer += 1
            a_num = 0
    if a_num == 0:
        answer += 2
    elif a_num == 1:
        answer += 1
    return answer


print(solution("a"))