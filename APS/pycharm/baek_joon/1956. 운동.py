V, E = map(int, input().split())
ad_matrix = [[False] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    ad_matrix[a-1][b-1] = c
for i in range(V):
    for j in range(V):
        if ad_matrix[i][j]:
            for k in range(V):
                if ad_matrix[j][k]:
                    if ad_matrix[i][k]:
                        ad_matrix[i][k] = min(ad_matrix[i][k], ad_matrix[i][j]+ad_matrix[j][k])
                    else:
                        ad_matrix[i][k] = ad_matrix[i][j] + ad_matrix[j][k]
result = 4000000
for i in range(V):
    if ad_matrix[i][i]:
        if ad_matrix[i][i] < result:
            result = ad_matrix[i][i]
if result == 4000000:
    result = -1
print(result)
