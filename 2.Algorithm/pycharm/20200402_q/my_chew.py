q = []

for _ in range(20):
    q.append([_+1, 0])
    temp = q.pop(0)
    temp[1] *= 2
    q.append(temp)


print(len(q))
print(_)
for que in q:
    print(que[1])
