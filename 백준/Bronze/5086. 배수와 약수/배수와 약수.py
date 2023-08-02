while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    answer = ''

    if B % A == 0:
        answer = "factor"

    elif A % B == 0:
        answer = "multiple"

    else:
        answer = "neither"

    print(answer)

