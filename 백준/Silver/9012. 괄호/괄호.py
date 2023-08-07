T = int(input())

for tc in range(1, T + 1):
    lst = list(input())

    cnt = 0
    for item in lst:
        if item == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            print("NO")
            break

    if cnt == 0:
        print("YES")
    if cnt > 0:
        print("NO")














