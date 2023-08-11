import sys
input = sys.stdin.readline

M = int(input())

my_set = set()
for _ in range(M):
    input_lst = list(input().split())
    if len(input_lst) == 2:
        a = input_lst[0]
        b = int(input_lst[1])
    else:
        a = input_lst[0]

    if a == 'add':
        my_set.add(b)

    elif a == 'remove':
        if b in my_set:
            my_set.remove(b)

    elif a == 'check':
        if b in my_set:
            print(1)
        else:
            print(0)

    elif a == 'toggle':
        if b in my_set:
            my_set.remove(b)
        else:
            my_set.add(b)

    elif a == 'all':
        my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

    elif a == 'empty':
        my_set.clear()
