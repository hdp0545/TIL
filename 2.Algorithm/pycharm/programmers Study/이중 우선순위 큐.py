import heapq


def solution(operations):
    que = []
    for operation in operations:
        command, target = operation.split(' ')
        if command == "I":
            heapq.heappush(que, int(target))
            print(que)
        if command == "D":
            if len(que) > 0:
                if target == "-1":
                    print(heapq.heappop(que))
                else:
                    print(que.pop())
    answer = []
    return answer


print(solution(["I 16", "I 5", "I -3", "D -1"]))