x1, y1 = map(int, input().split())

x_lst = [x1]
y_lst = [y1]

for _ in range(2):
    x, y = map(int, input().split())

    if x in x_lst:
        x_lst.remove(x)
    else:
        x_lst.append(x)

    if y in y_lst:
        y_lst.remove(y)
    else:
        y_lst.append(y)

print(x_lst[0], y_lst[0])