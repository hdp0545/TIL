class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addLast(self, new):
        if self.head is None:
            self.head = new
            new.prev = new.next = new
        else:
            tail = self.head.prev
            new.prev = tail
            new.next = self.head
            tail.next = new
            self.head.prev = new
        self.size += 1

    def printList(self):
        if self.head is None:
            return
        cur = self.head.prev
        for i in range(self.size):
            print(cur.data, end=' ')
            cur = cur.prev
            if i >= 9:
                break
        print()


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    mylist = LinkedList()
    arr = map(int, input().split())
    for val in arr:
        mylist.addLast(Node(val))

    cur = mylist.head
    for _ in range(K):
        for _ in range(M):
            cur = cur.next

        prev = cur.prev
        new = Node(prev.data + cur.data, prev, cur)
        prev.next = new
        cur.prev = new
        cur = new
        mylist.size += 1
    print('#', tc, sep='', end=' ')
    mylist.printList()