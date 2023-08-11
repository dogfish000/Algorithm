T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    fashion_dic = {}

    for _ in range(n):
        a, b = input().split()
        fashion_dic[b] = fashion_dic.get(b, 1) + 1

    lst = list(fashion_dic.values())

    value = 1

    for item in lst:
        value *= item

    print(value - 1)