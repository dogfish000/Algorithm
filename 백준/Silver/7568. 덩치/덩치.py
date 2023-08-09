import sys
input = sys.stdin.readline

N = int(input())

spec_lst = []
rank_lst = [0] * N

for _ in range(N):
    tmp = list(map(int, input().split()))
    spec_lst.append(tmp)

for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue

        if spec_lst[j][0] > spec_lst[i][0] and spec_lst[j][1] > spec_lst[i][1]:
            cnt += 1

    rank_lst[i] = cnt + 1

print(*rank_lst)
