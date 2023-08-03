N = int(input())

answer = 0

for i in range(1, N):
    K = i
    total = i
    while K >= 1:
        total += K % 10
        K = K // 10
    if total == N:
        answer = i
        break

print(answer)
