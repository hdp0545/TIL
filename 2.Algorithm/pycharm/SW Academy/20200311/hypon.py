answer = []
for tc in range(1, int(input())+1):
    word = input()
    H = int(input())
    location = list(map(int, input().split()))
    check = [0] * (len(word) + 1)
    for i in location:
        check[i] += 1
    result = ''
    for i in range(len(word)):
        result += '-' * check[i]
        result += word[i]
    result += '-' * check[len(word)]
    answer.append('#{} {}'.format(tc, result))
print('\n'.join(answer))