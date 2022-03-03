# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    M = len(S[0])
    for i in range(M):
        visit = ['F'] * 26
        for idx, s in enumerate(S):
            n = ord(s[i]) - ord('a')
            if visit[n] == 'F':
                visit[n] = idx
            else:
                return [visit[n], idx, i]
    return []

print(solution(['abc', 'bca', 'dbe']))