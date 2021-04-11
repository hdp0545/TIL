for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    if N < M:
        cnt = 0
        while N < M:
            N <<= 1
            cnt += 1
        if M < (N*3)//4:
            cnt -= 1
            N >>= 1
        over_stack = [1 << i for i in range(cnt+1)]
        lower_stack = [N]
        lower_stack += [1 << i for i in range(cnt, -1, -1)]
        for i in range(cnt+1):
            over_stack.append(10 << i)
        over_stack.sort(reverse=True)
        diff = N - M
        while diff:
            my_min = abs(diff)
            if diff > 0:
                for over in over_stack:
                    if abs(diff - over) < my_min:
                        my_min = diff - over
                    if diff - over > 0:
                        break
            else:
                for lower in lower_stack:
                    if abs(diff + lower) < my_min:
                        my_min = diff + lower
                    if diff + lower < 0:
                        break
            cnt += 1
            diff = my_min
        print(f'#{tc} {cnt}')
    else:
        res = (N - M) // 10 + (N - M) % 10
        print(f'#{tc} {res}')
