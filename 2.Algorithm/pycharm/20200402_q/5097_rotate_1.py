class Circle_queue: # 클래스 생성
    def __init__(self, N):
        self.value = [None] * (N + 1)
        self.le = (N + 1)
        self.front = 0
        self.rear = 0

    def enqueue(self, elem): # 메서드 enqueue 정의
        if (self.rear + 1) % self.le == self.front: #isFull
            return "Queue_Full"
        else:
            self.rear = (self.rear + 1) % self.le
            self.value[self.rear] = elem

    def dequeue(self): # 메서드 dequeue 정의
        if self.front == self.rear:
            return "Queue_Empty"
        else:
            self.front = (self.front + 1) % self.le
            return self.value[self.front]

    def check(self, number=0): # 첫번째 항목 찾기
        if number < self.le:
            return self.value[(self.front + 1 + number) % self.le]
        else:
            return "Index_Error"

    def show(self): # 전체 보여주기
        return [self.value[(self.front + 1 + i) % self.le] for i in range(self.le)]


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = list(input().split())
    q = Circle_queue(N) # 인스턴스 생성
    for d in data:
        q.enqueue(d) # data의 자료를 q에 넣어줌.

    for _ in range(M):
        temp = q.dequeue() # 빼고 temp에 저장 후,
        q.enqueue(temp) # temp를 q에 저장.
    print('#{} {}'.format(tc, q.check()))
