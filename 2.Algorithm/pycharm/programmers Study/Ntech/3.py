# Case 1
t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
t2 = [[1,2],[-1,-1],[-1,-1]]
right_answer = 2

# Case 2
# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[-1, 1], [-1, -1]]
# right_answer = 1

# Case 3
# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[1, 2], [-1, 5], [3, 4], [-1, -1], [-1, -1], [-1, -1]]
# right_answer = 1

# # Case 4
# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[-1, -1]]
# right_answer = 5

def same_node(a, b):
    if a[0] * b[0] < 0 or a[1] * b[1] < 0:
        return False
    return True


parents = [0]
cnt = 0

for a, b in t1:
    if a != -1:
        parents.append(a)
    if b != -1:
        parents.append(b)
print(parents)

for parent in parents:
    pqueue = [parent]
    queue = [0]

    flag = 0
    while queue:
        top1 = pqueue.pop(0)
        top2 = queue.pop(0)

        if not same_node(t1[top1], t2[top2]):
            flag = 1
            break

        for node in t1[top1]:
            if node != -1:
                pqueue.append(node)

        for node in t2[top2]:
            if node != -1:
                queue.append(node)

        if len(pqueue) != len(queue):
            flag = 1
            break

    if not flag:
        print('== Correct Case ==')
        print('parent:', parent)
        cnt += 1

print('====')
if right_answer == cnt:
    print('Correct')
    print('And the andswer is:', cnt)
else:
    print('Naah')