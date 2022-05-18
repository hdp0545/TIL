class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# data = (id, amount, price)
class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
        self.current = None

    def __len__(self):
        return self.length

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data

    def add_first(self, data):
        cur = self.head
        self.head = Node(data, cur)
        self.length += 1

    def append(self, data):
        cur = self.head
        if cur:
            while cur.next:
                cur = cur.next
            cur.next = Node(data)
            self.length += 1
        else:
            self.add_first(data)

    def pop(self):
        if self.head is not None:
            temp = self.head.data
            self.head = self.head.next
            return temp
        else:
            return (0, 0, 0)

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1

    def pending(self, data):
        cur = self.head
        if cur:
            if cur.data[2] < data[2]:
                self.add_first(data)
            else:
                while cur.next:
                    if cur.next.data[2] < data[2]:
                        break
                    cur = cur.next
                cur.next = Node(data, cur.next)
                self.length += 1
        else:
            self.add_first(data)





def solution(req_id, req_info):
    answer = []
    N = len(req_id)
    pending_buy = LinkedList()
    pending_sell = LinkedList()
    table = {id : [0, 0] for id in req_id}  # amount, price
    for i in range(N):
        t, amount, price = req_info[i]
        if t: # 판매요청
            sell_amount = amount
            sell_price = price
            sell_id = req_id[i]
            while sell_amount > 0:
                buy_id, buy_amount, buy_price = pending_buy.pop()
                if buy_price < sell_price:
                    break
                else:
                    # 수량 정하기
                    amount = min(buy_amount, sell_amount)
                    # 계좌 이동
                    table[sell_id][0] -= amount
                    table[sell_id][1] += amount * sell_price
                    table[buy_id][0] += amount
                    table[buy_id][1] -= amount * sell_price
                    # 수량제거
                    buy_amount -= amount
                    sell_amount -= amount
                    if buy_amount:
                        pending_buy.add_first((buy_id, buy_amount, buy_price))
            if sell_amount:
                pending_sell.pending((sell_id, sell_amount, -sell_price))
        else: # 구매요청
            buy_amount = amount
            buy_price = price
            buy_id = req_id[i]
            while buy_amount > 0:
                sell_id, sell_amount, sell_price = pending_sell.pop()
                sell_price = -sell_price
                if buy_price < sell_price:
                    break
                else:
                    # 수량 정하기
                    amount = min(buy_amount, sell_amount)
                    # 계좌 이동
                    table[sell_id][0] -= amount
                    table[sell_id][1] += amount * sell_price
                    table[buy_id][0] += amount
                    table[buy_id][1] -= amount * sell_price
                    # 수량제거
                    buy_amount -= amount
                    sell_amount -= amount
                    if sell_amount:
                        pending_sell.add_first((sell_id, sell_amount, -sell_price))
            if buy_amount:
                pending_buy.pending((buy_id, buy_amount, buy_price))
    for key, value in table.items():
        amount, price = value
        if amount > 0:
            key += ' +' + str(amount)
        else:
            key += ' ' + str(amount)
        if price > 0:
            key += ' +' + str(price)
        else:
            key += ' ' +str(price)
        answer.append(key)
    answer.sort()
    return answer

print(solution(["William", "Andy", "Rohan", "Rohan", "Louis", "Andy"], [[1, 7, 20], [0, 10, 10], [1, 10, 40], [1, 4, 25], [0, 5, 11], [0, 20, 30]]))
