def solution(cookies, k):
    cookie_n = len(cookies)
    cnt = [1] * cookie_n
    stack = [[j] for j in cookies]
    for i in range(cookie_n-1, -1, -1):
        temp = 0
        temp_stack = []
        for j in range(i + 1, cookie_n):
            if cookies[i] < cookies[j] and temp <= cnt[j]:
                temp = cnt[j]
                stack[i].append(stack[j])

        cnt[i] += temp
    print(cnt)
    max_cnt = max(cnt)
    cnt_stack = []
    for i in range(cookie_n):
        if cnt[i] == max_cnt:
            cnt_stack.append(i)
    answer = []
    print(stack)
    return


print(solution([1,4,2,6,5,3], 2))