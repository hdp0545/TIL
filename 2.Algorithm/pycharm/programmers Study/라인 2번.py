from itertools import product

def solution(sentences, n):
    answer = 0
    score_need = []
    for sentence in sentences:
        score = len(sentence)
        is_used = [False] * 27
        needs = []
        sen = list(set(sentence))
        for word in sen:
            if word != ' ':
                if 64 < ord(word) < 91:
                    word = word.lower()
                    score += 1
                    if not is_used[26]:
                        is_used[26] = True
                        needs.append('shift')
                idx = ord(word) - 97
                if not is_used[idx]:
                    is_used[idx] = True
                    needs.append(word)
        score_need.append([score, needs])

    answers = []
    for bools in product([True, False], repeat=len(sentences)):
        check = [False] * 27
        score = 0
        cnt = 0
        for i in range(len(sentences)):
            if bools[i]:
                score += score_need[i][0]
                for word in score_need[i][1]:
                    if word == 'shift':
                        if not check[26]:
                            check[26] = True
                            cnt += 1
                    else:
                        idx = ord(word) - 97
                        if not check[idx]:
                            check[idx] = True
                            cnt += 1
        if cnt <= n:
            answer = max(answer, score)
    return answer


print(solution(["line in line", "LINE", "in lion"], 5))