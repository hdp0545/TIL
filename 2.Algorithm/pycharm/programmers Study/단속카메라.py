def solution(routes):
    peaks = []
    routes.sort()
    for route in routes:
        start, end = route
        for peak in peaks:
            ts, te = peak
            if ts <= end and start <= te:
                peak[0] = max(start, ts)
                peak[1] = min(end, te)
                break
        else:
            peaks.append(route)
    answer = len(peaks)
    return answer


print(solution([[1, 5], [3, 4], [2, 3], [1, 3], [7, 8], [6, 7], [7, 9], [5, 10]]))