import sys
sys.stdin = open("in.txt","r")
sys.stdout = open("out.txt","w")
def check(arr):
    for p in range(100):
        temp = arr[p]
        for q in range(100, 0, -1): # 문자열 길이
            for r in range(100 - q + 1): # 시작점
                if temp[r:r+q] == temp[r:r+q][::-1]:
                    return q
for test_case in range(10):
    input()
    arr = []
    for i in range(100):
        arr.append(input())
    answer1 = check(arr)
    changed_arr = []
    for j in range(100):
        temp = ''
        for i in range(100):
            temp += arr[i][j]
        changed_arr.append(temp)
    # changed_arr = [['' for _ in range(100)] for _ in range(100)]
    #
    # for i in range(100):
    #     for j in range(100):
    #         changed_arr[i][j] = arr[j][i]
    answer2 = check(changed_arr)
    print('answer1, answer2', answer1, answer2)
    answer = max(answer1, answer2)
    print('#{} {}'.format(test_case + 1, answer))