import math

d = 10000

check_lst = [0] * (d + 1)

for i in range(1, d):
    if check_lst[i] == 0:
        print(i)

    tmp = i

    while i >= 1:
        tmp += i % 10
        i = math.floor(i / 10)

    if tmp <= d:
        check_lst[tmp] = 1



