N, M = map(int, input().split())

lst1 = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    lst1.append(tmp)

lst2 = []

for _ in range(N):
    tmp = list(map(int, input().split()))
    lst2.append(tmp)

lst_add = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        lst_add[i][j] = lst1[i][j] + lst2[i][j]

for i in range(N):
    print(*lst_add[i])