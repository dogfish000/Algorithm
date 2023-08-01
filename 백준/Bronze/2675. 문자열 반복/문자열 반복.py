T = int(input())

for tc in range(1, T + 1):
    R, S = map(str, input().split())
    r = int(R)
    P = ''

    for s in S:
        for _ in range(r):
            P += s

    print(P)
