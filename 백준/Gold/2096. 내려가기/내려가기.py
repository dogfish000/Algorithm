import sys
input = sys.stdin.readline

N = int(input())

min_lst = []
max_lst = []
for i in range(N):
    tmp = list(map(int, input().split()))
    min_lst.append(tmp.copy())
    max_lst.append(tmp.copy())


for i in range(1, N):
    min_lst[i][0] = min_lst[i][0] + min(min_lst[i - 1][0], min_lst[i - 1][1])
    min_lst[i][1] = min_lst[i][1] + min(min_lst[i - 1][0], min_lst[i - 1][1], min_lst[i - 1][2])
    min_lst[i][2] = min_lst[i][2] + min(min_lst[i - 1][1], min_lst[i - 1][2])

    max_lst[i][0] = max_lst[i][0] + max(max_lst[i - 1][0], max_lst[i - 1][1])
    max_lst[i][1] = max_lst[i][1] + max(max_lst[i - 1][0], max_lst[i - 1][1], max_lst[i - 1][2])
    max_lst[i][2] = max_lst[i][2] + max(max_lst[i - 1][1], max_lst[i - 1][2])


min_val = min(min_lst[-1])
max_val = max(max_lst[-1])


print(max_val, min_val)




