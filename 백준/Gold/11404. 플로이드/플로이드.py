import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = 987654321

lst = [[INF] * (N + 1) for _ in range(N + 1)]


for i in range(1, N + 1):
    lst[i][i] = 0


for _ in range(M):
    s, e, k = map(int, input().split())
    if k < lst[s][e]:
        lst[s][e] = k


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j < N:
            if lst[i][j] == INF:
                lst[i][j] = 0
            print(lst[i][j], end=' ')
        else:
            if lst[i][j] == INF:
                lst[i][j] = 0
            print(lst[i][j])
