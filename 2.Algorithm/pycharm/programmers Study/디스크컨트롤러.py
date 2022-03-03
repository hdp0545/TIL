import heapq

def solution(jobs):
    tot = 0
    jobs.sort(key=lambda x:x[1])
    jobs.sort()
    time = 0
    stack = []
    for job in jobs:
        if job[0] < time:
            heapq.heappush(stack, (job[1], job[0]))
        else:
            flag = 1
            if job[0] == time:
                heapq.heappush(stack, (job[1], job[0]))
                flag = 0
            while stack:
                du, st = heapq.heappop(stack)
                if time >= st:
                    time += du
                else:
                    time = st + du
                tot += time - st
                if time >= job[0]:
                    break
            if flag:
                heapq.heappush(stack, (job[1], job[0]))
    while stack:
        du, st = heapq.heappop(stack)
        if time >= st:
            time += du
        else:
            time = st + du
        tot += time - st
    return tot // len(jobs)

print(solution([[0, 3], [1, 9], [500, 6]]))