import sys

N = int(sys.stdin.readline().rstrip())

lst = []

for _ in range(N):
    a = sys.stdin.readline().rstrip()

    if "push" in a:
        c, d = (a.split())

        lst.append(int(d))

    if a == "top":
        if len(lst) == 0:
            print(-1)

        else:
            print(lst[len(lst) - 1])

    if a == "pop":
        if len(lst) == 0:
            print(-1)

        else:
            tmp = lst[-1]
            lst = lst[0:len(lst) - 1]
            print(tmp)

    if a == "size":
        print(len(lst))

    if a == "empty":
        if len(lst) == 0:
            print(1)

        else:
            print(0)
