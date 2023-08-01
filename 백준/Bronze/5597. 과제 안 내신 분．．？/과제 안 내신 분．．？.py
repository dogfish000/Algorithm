num_lst = []

for _ in range(30):
    num_lst.append(0)


for _ in range(28):
    idx = int(input())
    num_lst[idx - 1] = 1


for i in range(len(num_lst)):
    if num_lst[i] == 0:
        print(i + 1)