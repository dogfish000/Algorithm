lst = []
max_col = 0

answer = ''


for i in range(5):
    tmp = list(input())
    max_col = max(max_col, len(tmp))
    lst.append(tmp)

for j in range(max_col):
    for i in range(5):
        if j > len(lst[i]) - 1:
            continue

        answer += lst[i][j]

print(answer)