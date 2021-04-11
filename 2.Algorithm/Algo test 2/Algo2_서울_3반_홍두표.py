for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    children = [set(list(map(int, input().split()))[1:]) for _ in range(N)] # input 사탕 종류로만 받기
    result = 0 # 초기결과값 설정
    for child in children: # 아이들이 갖고 있는 사탕의 종류 세기
        result += len(child)
    targets = sorted(children[:M], key=lambda x: len(x), reverse=True) # 사탕 나누어 줄 학생들 타겟으로 받기
    rest_candy = [1] * M        # 남은 사탕들 갯수 저장하기
    for target in targets:      # 사탕을 나누어 줄 학생들 중에서
        for candy in range(1, M+1):     # 캔디 종류들 중에
            if candy not in target:     # 없는 캔디가 있고
                if rest_candy[candy-1]:     # 그 캔디가 남아 있으면
                    rest_candy[candy-1] = 0 # 남은 캔디수를 없애고
                    result += 1             # 결과 종류를 하나 늘린다.
                    break
    print(f'#{tc} {result}')