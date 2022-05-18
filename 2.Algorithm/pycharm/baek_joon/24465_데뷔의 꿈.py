stars = [True] * 12

def find_star(m, d):
    temp = m * 100 + d
    star = 11
    if 120 <= temp < 219:
        star = 0
    elif 219 <= temp < 321:
        star = 1
    elif 321 <= temp < 420:
        star = 2
    elif 420 <= temp < 521:
        star = 3
    elif 521 <= temp < 622:
        star = 4
    elif 622 <= temp < 723:
        star = 5
    elif 723 <= temp < 823:
        star = 6
    elif 823 <= temp < 923:
        star = 7
    elif 923 <= temp < 1023:
        star = 8
    elif 1023 <= temp < 1123:
        star = 9
    elif 1123 <= temp < 1222:
        star = 10
    return star

for _ in range(7):
    m, d = map(int, input().split())
    star = find_star(m, d)
    stars[star] = False

N = int(input())
answers = []
for _ in range(N):
    m, d = map(int, input().split())
    star = find_star(m, d)
    if stars[star]:
        answers.append((m, d))
if answers:
    answers.sort()
    for answer in answers:
        m, d = answer
        print(m, d)
else:
    print('ALL FAILED')
