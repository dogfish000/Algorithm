N, K = map(int, input().split())

lst = []
cnt_lst = [0] * N
answer_lst = []

for i in range(N):
    lst.append(i + 1)

idx = 0

while len(lst) > 0:

    idx = idx + K - 1
    if idx > len(lst) - 1:
        idx = idx % len(lst)

    answer_lst.append(lst.pop(idx))

print("<", end="")
print(*answer_lst, sep=', ', end='')
print(">")
