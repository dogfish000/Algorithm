T = int(input())



for tc in range(1, T + 1):
    N, M = map(int, input().split())

    lst1 = []

    for i in range(N):
        lst1.append(i)

    lst2 = list(map(int, input().split()))

    printer = list(zip(lst1, lst2))

    cnt = 0

    while True:
        max_idx = -1
        max_val = 0
        for i in range(len(printer)):
            if printer[i][1] > max_val:
                max_val = printer[i][1]
                max_idx = i

        if max_idx != 0:
            for i in range(max_idx):
                printer.append(printer.pop(0))


        if printer[0][0] == M:
            cnt += 1
            break
        else:
            printer.pop(0)
            cnt += 1

    print(cnt)