# # Case 1
# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[1,2],[-1,-1],[-1,-1]]
# right_answer = 2

# # Case 2
# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[-1, 1], [-1, -1]]
# right_answer = 1

# # Case 3
# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[1, 2], [-1, 5], [3, 4], [-1, -1], [-1, -1], [-1, -1]]
# right_answer = 1

# # Case 4
# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[-1, -1]]
# right_answer = 5

# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[1,2],[-1,-1],[-1,-1]]
# right_answer = 2

def same_node(target, goal, i):
    stack = [(i, 0)]
    while stack:
        t_i, g_i = stack.pop()
        if target[t_i][0] * goal[g_i][0] < 0 or target[t_i][1] * goal[g_i][1] < 0 :
            return False
        else:
            if target[t_i][0] > 0:
                stack.append((target[t_i][0], goal[g_i][0]))
            if target[t_i][1] > 0:
                stack.append((target[t_i][1], goal[g_i][1]))
    return True

def solution(t1, t2):
    answer = 0
    for i in range(len(t1)):
        if same_node(t1, t2, i):
            answer += 1
    return answer

print(solution(t1, t2))