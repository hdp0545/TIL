def solution(s):
    N = len(s)
    answer = N
    for n in range(1, N//2 + 1):
        start = 0
        end = n
        cnt = 0
        stack = []
        while start <= N-n:
            if s[start:start+n] == s[end:end+n]:
                cnt += 1
            else:
                if cnt:
                    stack.append(cnt)
                    cnt = 0
            start += n
            end += n
        temp = ''
        for word in stack:
             word += 1
             temp += str(word)
        answer = min(answer, N + len(temp) - (sum(stack) * n))
    return answer

text = "a" * 100
print(solution(text))