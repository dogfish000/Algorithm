T = int(input())

for tc in range(1, T + 1):
    C = int(input())

    coin_lst = []

    coin_lst.append(C // 25)
    C = C % 25

    coin_lst.append(C // 10)
    C = C % 10

    coin_lst.append(C // 5)
    C = C % 5

    coin_lst.append(C)

    print(*coin_lst)
