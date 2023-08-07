N = int(input())

lst = []

for _ in range(1, N + 1):
    lst.append(list(map(int, input().split())))


sort_lst = sorted(lst, key=lambda x: (x[0], x[1]))

for i in range(N):
    print(*sort_lst[i])

