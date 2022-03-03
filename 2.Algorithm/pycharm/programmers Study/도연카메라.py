def solution(routes):
    # 답
    answer = 0

    # 겹치는 개수가 적은 요소부터 정렬하여 stack에 있으면 지우고, 없으면 넘어갈 리스트
    del_list = [[i] for i in range(len(routes))]

    # 인덱스 모아놓고 하나씩 지워갈 리스트
    stack = [i for i in range(len(routes))]

    # 겹치는 요소들을 각 인덱스에 추가
    for i in range(len(routes)):
        for j in range(len(routes)):
            if i != j:
                if routes[i][1] >= routes[j][0] and routes[i][0] <= routes[j][1]:
                    del_list[i].append(j)

    # print(del_list)

    # 겹치는게 적은 요소부터 나열한 뒤, 지워나갈 예정
    for i in range(len(del_list) - 1):
        for j in range(i + 1, len(del_list)):
            if len(del_list[i]) > len(del_list[j]):
                temp = del_list[i]
                del_list[i] = del_list[j]
                del_list[j] = temp



    del_list.sort(key=len)
    # print(del_list)

    # 겹치는게 적은 요소부터 지우면서 카메라 수도 1개씩 증가
    for i in range(len(del_list)):
        flag = True
        for j in range(len(del_list[i])):
            if del_list[i][j] in stack:
                stack.remove(del_list[i][j])
                flag = False
        # 삭제한거 있으면 플래그로 반응하여 카메라 추가
        if flag == False:
            answer += 1
        if len(stack) == 0:
            # print("i:%d break" %i)
            break

    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))