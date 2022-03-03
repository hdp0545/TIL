def find(q):
    n = len(q)
    s, e = 0, n-1
    while s < e:
        m = (s + e) // 2
        s, e = (s, m) if q[m] == "?" else (m + 1, e)
    return e


def solution(words, queries):
    answer = []
    dict_target = {}
    dict_reverse = {}
    for word in words:
        if len(word) in dict_target:
            dict_target[len(word)].append(word)
            dict_reverse[len(word)].append(word[::-1])
        else:
            dict_target[len(word)] = [word]
            dict_reverse[len(word)] = [word[::-1]]
    for key in dict_target.keys():
        dict_target[key].sort()
        dict_reverse[key].sort()
    for query in queries:
        n = len(query)
        if n in dict_target:
            if query[0] == "?":
                query = query[::-1]
                target = dict_reverse[n]
            else:
                target = dict_target[n]
            N = len(target)
            i = find(query)
            start = -1
            temp = query[:i] + ("{" * (n - i))
            end = N - 1
            while start < end:
                mid = (start + end + 1) // 2
                start, end = (mid, end) if target[mid] < query else (start, mid - 1)
            s = start + 1
            start = -1
            end = N - 1
            while start < end:
                mid = (start + end + 1) // 2
                start, end = (mid, end) if target[mid] <= temp else (start, mid - 1)
            answer.append(start - s + 1)
        else:
            answer.append(0)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["aaaa?", "????o", "fr???", "fro???", "pro?"]))