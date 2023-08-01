lst = []

for _ in range(9):
    tmp = list(map(int, input().split()))
    lst.append(tmp)


max_value = -1
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if lst[i][j] > max_value:
            max_value = lst[i][j]
            row = i + 1
            col = j + 1

print(max_value)
print(row, col)