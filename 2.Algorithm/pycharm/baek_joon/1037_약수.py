N = int(input())
if N == 1:
    a = int(input())
    print(a * a)
else:
    a_list = list(map(int, input().split()))
    a_list.sort()
    print(a_list[0] * a_list[-1])