class Node:
    def __init__(self, d=0, n=None):
        self.data = d
        self.next = n


class LinkedList:
    def __init__(self):
        Head = Node('Head')
        self.head = Head
        self.size = 0

    def insert(self, idx, data):
        new = Node(data)
        cur = self.head
        for i in range(idx):
            cur = cur.next
        new.next = cur.next
        cur.next = new
        self.size += 1

    def search(self, idx):
        cur = self.head
        for i in range(idx):
            cur = cur.next
        return cur.next.data


for _ in range(int(input())):
    N, M, L = map(int, input().split())
    arr = list(input().split())
    mylist = LinkedList()
    for i in range(N):
        mylist.insert(i, arr[i])
    for j in range(M):
        idx, data = map(int, input().split())
        mylist.insert(idx, data)
    print(f'#{_ + 1} {mylist.search(L)}')