for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    friends_list = [[] for _ in range(N+1)]
    invited_friend = [False] * (N + 1)
    invited_friend[1] = True
    for _ in range(M):
        f1, f2 = map(int, input().split())
        friends_list[f1].append(f2)
        friends_list[f2].append(f1)
    result = 0
    dq = []
    for friend in friends_list[1]:
        if not invited_friend[friend]:
            dq.append(friend)
            invited_friend[friend] = True
            result += 1
    while dq:
        friend2 = dq.pop()
        for friend in friends_list[friend2]:
            if not invited_friend[friend]:
                invited_friend[friend] = True
                result += 1
    print(f'#{tc} {result}')