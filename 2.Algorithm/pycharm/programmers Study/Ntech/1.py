
def solution(flowers):
    answer = 0
    periods = set()
    while flowers:
        start, end = flowers.pop()
        for i in range(start, end):
            periods.add(i)
    answer = len(periods)
    return answer