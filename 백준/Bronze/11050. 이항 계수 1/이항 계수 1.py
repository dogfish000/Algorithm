N, K = map(int, input().split())

top_num = 1
top_cnt = 0
for i in range(N, 0, -1):
    if top_cnt == N - K:
        break
    top_num *= i
    top_cnt += 1

bot_num = 1
for i in range(N - K, 0, -1):
    bot_num *= i

answer = int(top_num / bot_num)

print(answer)
