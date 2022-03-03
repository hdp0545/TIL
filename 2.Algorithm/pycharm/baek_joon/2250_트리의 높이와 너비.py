class tree:
    def __init__(self, p=-1, l=-1, r=-1, i=-1):
        self.left = l
        self.right = r
        self.parent = p
        self.idx = i

def find_left(i):
    while True:
        j = trees[i].left
        if j == -1:
            break
        else:
            i = j
    return i

def find_root(i):
    while True:
        j = trees[i].parent
        if j == -1:
            break
        else:
            i = j
    return i

N = int(input())
trees = [0] * (N+1)
for _ in range(N):
    s, l, r = map(int, input().split())
    trees[s] = tree(-1, l, r)

for w in range(1, N+1):
    node = trees[w]
    if node.left != -1:
        trees[node.left].parent = w
    if node.right != -1:
        trees[node.right].parent = w

root = find_root(1)
i = find_left(root)
idx = 1

while i != -1:
    node = trees[i]
    if node.idx == -1:
        node.idx = idx
        i = node.parent
        idx += 1
        if node.right != -1:
            i = find_left(node.right)
    else:
        i = node.parent

level_list = [root]
max_level = 0
level = 0
max_length = 0
while level_list:
    temp_list = []
    level += 1
    left = N
    right = 0
    for i in level_list:
        if trees[i].left != -1: temp_list.append(trees[i].left)
        if trees[i].right != -1: temp_list.append(trees[i].right)
        if trees[i].idx < left:
            left = trees[i].idx
        if trees[i].idx > right:
            right = trees[i].idx
    length = right - left + 1
    if max_length < length:
        max_length = length
        max_level = level
    level_list = temp_list

print(max_level, max_length)