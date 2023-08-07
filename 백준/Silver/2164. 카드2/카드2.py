N = int(input())

if N == 1:
    print(1)
else:
    cnt = 1
    while N > 2 ** cnt:
        cnt += 1

    answer = 2 * (N - (2 ** (cnt - 1)))
    print(answer)