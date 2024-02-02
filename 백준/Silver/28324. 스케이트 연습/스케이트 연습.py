N = int(input())

speed = list(map(int, input().split()))



ans = [0] * N

ans[-1] = 1



for i in range(N - 1, 0, -1):
    if speed[i - 1] >= (ans[i] + 1):
        ans[i - 1] = (ans[i] + 1)
    else:
        ans[i - 1] = speed[i -1]


print(sum(ans))

