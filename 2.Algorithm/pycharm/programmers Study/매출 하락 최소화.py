class tree():
    def __init__(self, s=0, p=-1):
        self.sale = s
        self.parent = p
        self.answer = 0
        self.children = []

    def solve_answer(self):
        if self.children:
            sum = 0
            temp = []
            # 팀원들의 매출액 중 가장 작은 값
            for child in self.children:
                a, b = child       # sale, answer
                temp.append(a - b)
                sum += b
            sum += min(temp)       # 모두 answer(최적해)를 더했지만 적어도 하나는 sale을 더해야 함.
            self.answer = min(self.sale, sum)


def solution(sales, links):
    N = len(sales)
    # 트리구조 생성 및 각 사원들의 매출액 넣기
    nodes = [tree(sale) for sale in sales]
    # 맨 자식 노드 판별
    checks = [[] for _ in range(N)]  # 각 팀장의 팀원들
    # links를 돌며 부모와 자식 구조 넣기
    for link in links:
        a, b = link  # a: 팀장, b: 팀원
        nodes[b-1].parent = a
        checks[a-1].append(b-1)

    # 팀장부터 차례로 내려가며 스택 순서 쌏기
    temp = [0]
    stack = []
    while temp:
        a = temp.pop()
        stack.append(a)
        for b in checks[a]:
            temp.append(b)

    # 스택에서 아래에서 위로 쌓아가며 계산하기
    while stack:
        i = stack.pop()
        node = nodes[i]
        parent = nodes[node.parent - 1]
        node.solve_answer()
        parent.children.append((node.sale, node.answer))
        parent.sale += node.answer                      # 팀장의 매출액을 단순 매출액이 아닌 여태까지 총합의 매출액으로 바꾸기 위함
    answer = nodes[0].answer

    return answer

print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))