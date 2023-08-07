import sys

N = int(sys.stdin.readline().rstrip())

lst = []

for _ in range(N):
    a = sys.stdin.readline().rstrip()

    if "push_front" in a:
        c, d = (a.split())

        lst.insert(0, int(d))

    if "push_back" in a:
        c, d = (a.split())

        lst.append(int(d))

    if a == "pop_front":
        if len(lst) == 0:
            print(-1)

        else:
            print(lst.pop(0))

    if a == "pop_back":
        if len(lst) == 0:
            print(-1)

        else:
            print(lst.pop(len(lst) - 1))

    if a == "size":
        print(len(lst))

    if a == "empty":
        if len(lst) == 0:
            print(1)

        else:
            print(0)

    if a == "front":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])

    if a == "back":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[len(lst) - 1])
