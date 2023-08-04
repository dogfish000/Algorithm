T = int(input())

for tc in range(1, T + 1):
    lst = list(input())

    cnt = 0
    score = 0

    for i in range(len(lst)):
        if lst[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0

    print(score)


