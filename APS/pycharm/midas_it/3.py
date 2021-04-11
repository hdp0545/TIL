def solution(cookies, k):
    answer = []
    cookie_n = len(cookies)
    stack = [-1]
    max_cnt = 0
    cnt = 1
    while stack:
        t = stack.pop()
        cnt -= 1
        for i in range(t+1, cookie_n):
            if not stack or cookies[stack[-1]] < cookies[i]:
                stack.append(i)
                cnt += 1
            if cookie_n - stack[-1] - 1 < max_cnt - cnt:
                break
        if max_cnt == cnt:
            cookie_stack = [cookies[c] for c in stack]
            answer.append(cookie_stack)
        elif max_cnt < cnt:
            max_cnt = cnt
            answer = [[cookies[c] for c in stack]]
    answer.sort()
    return answer[k-1]

print(solution([1,4,2,5,6,3], 2))