from collections import deque

def solution(operations):
    lis = []
    for operation in operations:
        command, target = operation.split(' ')
        if command == "I":
            lis.append(int(target))
        else:
            if len(lis) > 0:
                lis.sort()
                if target == "-1":
                    lis.pop(0)
                else:
                    lis.pop()
    lis.sort()
    if len(lis) == 0:
        answer = [0, 0]
    elif len(lis) == 1:
        n = lis.pop()
        answer = [n, n]
    else:
        answer = [lis.pop(), lis.pop(0)]
    return answer


print(solution(["I 16", "I 5", "I -3", "D -1"]))