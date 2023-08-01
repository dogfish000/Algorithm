num_lst = []

N, M = map(int, input().split())

for _ in range(N):
    num_lst.append(0)


for _ in range(M):
    i, j, k = map(int, input().split())

    for q in range(i - 1, j):
        num_lst[q] = k


for i in range(len(num_lst)):
    print(num_lst[i], end=" ")