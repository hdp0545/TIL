from collections import deque
n = int(input())
m = list(map(int,input().split()))
data = []
m.sort()
queue =deque(m)
count = 0
maxs = 0

for i in range(1,len(m)):
    if m[i-1] < m[i]:
        count += 1
maxs = count
count = 0


for i in range(len(m)):
    a = queue.popleft()
    if len(data) == 0:
        data.append(a)
        continue
    if data[-1] < a:
        data.append(a)
    else:
        queue.appendleft(a)
        for idx,j in enumerate(queue):
            if data[-1] < j:
                t = queue.index(j)
                queue.remove(j)
                data.append(t)
                break
for i in range(1,len(data)):
    if data[i-1] < data[i]:
        count += 1
print(max(count,maxs))