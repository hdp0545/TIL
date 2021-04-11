import sys
sys.stdin = open('stylish_input.txt', 'r')

gwal_ho = ['(', '{', '[', ')', '}', ']']

def rcs(R, r):
    if R != r:
        if R == 0:
            return r
        else:
            return -1
    else:
        if R == l[3]:
            return r



for tc in range(1, int(input())+1):
    p, q = map(int, input().split())
    master_code = [input() for _ in range(p)]
    my_code = [input() for _ in range(q)]
    #R, C, S 갯수
    RCS_count = [0, 0, 0]
    arr = []
    for _ in range(p-1):
        words = master_code.pop()
        cnt = 0
        i = 0
        # 온점 갯수 세는 코드
        while words[i] == '.':
            i += 1
            cnt += 1
        #괄호 갯수 세는 코드
        while i < len(words):
            if not words[i].isalpha():
                for j in range(6):
                    if words[i] == gwal_ho[j]:
                        if j // 3:
                            RCS_count[j % 3] += 1
                        else:
                            RCS_count[j] -= 1
            i += 1
        arr.append(RCS_count + [cnt])
    RCS_count = [0, 0, 0]
    arr_target = []
    for j in range(q-1):
        i = 0
        words = my_code[j]
        while i < len(words):
            if not words[i].isalpha():
                for j in range(6):
                    if words[i] == gwal_ho[j]:
                        if j // 3:
                            RCS_count[j % 3] -= 1
                        else:
                            RCS_count[j] += 1
            i += 1
        arr_target.append(RCS_count[:])
    print(arr_target)

    #r, c, s 가능한 경우
    R, C, S = 0, 0, 0
    if arr:
        l = arr[0]
        for r in range(1, 21):
            if l[0] and r > l[3]:
                break
            for c in range(1, 21):
                if l[1] and c > l[3]:
                    break
                for s in range(1, 21):
                    if l[2] and s > l[3]:
                        break
                    for l in arr:
                        if r * l[0] + c * l[1] + s * l[2] != l[3]:
                            break
                    else:
                        # print(r, c, s, l[3])
                        R, C, S = rcs(R, r), rcs(C, c), rcs(S, s)
    # print('#', R, C, S)








