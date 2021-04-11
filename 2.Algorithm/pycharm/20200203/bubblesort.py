import sys

sys.stdin = open('1206input.txt', 'r')

for i in range(1, 11):
    T = int(input())
    heights = list(map(int, input().split()))
    result = 0
    for idx in range(2, T-2):
        if heights[idx] == max(heights[idx-2:idx+3]):
            sample = heights[idx-2:idx] + heights[idx+1:idx+3]
            result += heights[idx] - max(sample)

    print('#{} {}'.format(i, result))