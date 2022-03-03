import sys
sys.stdin = open('input.txt', 'r')


def backtrack(check, i, r, k=0):
    c = []
    global min1
    if r > min1:
        return
    if i == k:
        min1 = r
    else:
        for i in range(10):
            if check[i]:
                c.append(i)
        for i in range(10):
            check[c[i]] = False
            backtrack(check, k+1, r + prices[2] - plan[c[i]] - plan[c[i]+1] - plan[c[i]+2])
            check[c[i]] = True


for test_case in range(1, int(input()) + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    check = [True]*12
    plan = [prices[1] if plan[i] * prices[0] > prices[1] else plan[i] * prices[0] for i in range(12)]
    min1 = sum(plan)
    for i in range(1, 5):
        backtrack(check, i, min1)

    print('#{} {}'.format(test_case, min1))

