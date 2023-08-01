num_lst = []

for _ in range(9):
    num_lst.append(int(input()))


print(max(num_lst))
print(num_lst.index(max(num_lst)) + 1)