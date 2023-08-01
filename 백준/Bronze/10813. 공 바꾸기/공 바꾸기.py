num_lst = []

N, M = map(int, input().split())

for i in range(N):
    num_lst.append(i + 1)

for _ in range(M):
    i, j = map(int, input().split())
    num_lst[i - 1], num_lst[j - 1] = num_lst[j - 1], num_lst[i - 1]

print(*num_lst)