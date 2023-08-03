while True:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break

    if sum(lst) - max(lst) <= max(lst):
        print("Invalid")
    else:
        if lst[0] == lst[1] == lst[2]:
            print("Equilateral")
        elif lst[0] != lst[1] and lst[1] != lst[2] and lst[2] != lst[0]:
            print("Scalene")
        else:
            print("Isosceles")