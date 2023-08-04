T = int(input())

for tc in range(1, T + 1):
    k = int(input())
    n = int(input())

    apart = []

    for _ in range(k + 1):
        tmp = [0] * n
        apart.append(tmp)

    for i in range(len(apart)):
        for j in range(len(apart[0])):
            if j == 0:
                apart[i][j] = 1
            if i == 0:
                apart[i][j] = j + 1

    for i in range(1, k + 1):
        for j in range(1, n):
            apart[i][j] = apart[i - 1][j] + apart[i][j - 1]

    print(apart[k][n - 1])





