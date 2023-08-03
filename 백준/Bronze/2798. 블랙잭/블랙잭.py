N, M = map(int, input().split())

lst = list(map(int, input().split()))

sum_lst = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = lst[i] + lst[j] + lst[k]
            if total <= M:
                sum_lst.append(total)

print(max(sum_lst))
