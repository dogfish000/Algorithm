N = int(input())

cnt = 0
answer = 0

while N > 0:
    if cnt == 0:
        cnt += 1
        N = N - 1
        answer += 1

    else:
        N = N - 6 * cnt
        cnt += 1
        answer += 1

print(answer)
