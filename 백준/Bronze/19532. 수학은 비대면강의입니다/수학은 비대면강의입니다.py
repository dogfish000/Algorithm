lst = list(map(int, input().split()))

y1 = lst[1] * lst[3] - lst[4] * lst[0]

y2 = lst[2] * lst[3] - lst[5] * lst[0]

y = int(y2 / y1)

x1 = lst[0] * lst[4] - lst[3] * lst[1]

x2 = lst[2] * lst[4] - lst[5] * lst[1]

x = int(x2 / x1)

print(x, y)