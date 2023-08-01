
crt_lst = [1, 1, 2, 2, 2, 8]
cur_lst = list(map(int, input().split()))

dif_lst = []

for i in range(len(crt_lst)):
    dif = crt_lst[i] - cur_lst[i]
    dif_lst.append(dif)

print(*dif_lst)