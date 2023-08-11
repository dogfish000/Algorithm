T = int(input())

for tc in range(1, T + 1):

    lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    N = int(input())

    for _ in range(N - 10):
        lst.append(lst[-1] + lst[-5])


    print(lst[N - 1])