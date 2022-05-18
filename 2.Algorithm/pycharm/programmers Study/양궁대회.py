def solution(n, info):
    answer = [0] * 11
    stack = []
    appeach = 0
    for i, value in enumerate(info):
        if value:
            appeach += 10 - i
            point = (10 - i) * 2
            giv = point / (value + 1)
            stack.append([giv, point, value+1, i])
        else:
            stack.append([10-i, 10-i, 1, i])
    stack.sort(key=lambda x:x[-1])
    stack.sort(key=lambda x:x[0], reverse=True)
    temp = 0
    lion = 0
    #stack[2], stack[3] = stack[3], stack[2]
    stack.append([6.666666666666667, 20, 3, 0])
    print(stack)
    
    for s in stack:
        giv, point, value, i = s
        if n >= temp + value:
            temp += value
            lion += point
            answer[i] = value
    answer[10] += n - temp

    if lion <= appeach:
        answer = [-1]
    print(lion)
    return answer

print(solution(7, [2,1,1,1,1,1,0,0,0,0,0]), [0,2,2,0,1,0,0,0,0,0,0])
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]), [-1]    )
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]), [1,1,2,0,1,2,2,0,0,0,0])
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]	), [1,1,1,1,1,1,1,1,0,0,2])