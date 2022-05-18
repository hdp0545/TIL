def sol(N, num, target, lev, flag):
    if N == target:
        return lev
    elif lev > 8:
        return 9
    if flag:
        e = sol(N * 10 + num, num, target, lev + 1, True)
    else:
        e = 9
    a = sol(N+num, num, target, lev+1, False)
    b = sol(N*num, num, target, lev+1, False)
    c = sol(N//num, num, target, lev+1, False)
    d = sol(N-num, num, target, lev+1, False)
    return min(a,b,c,d,e)

def solution(N, number):
    answer = sol(N, N, number, 1, True)
    if answer == 9:
        return -1
    return answer

print(solution(7, 700))