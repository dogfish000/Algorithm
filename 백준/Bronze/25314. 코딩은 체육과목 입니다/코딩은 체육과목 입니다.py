N = int(input())

answer = ""

rep = N // 4

for _ in range(rep):
    answer += 'long '

answer += 'int'

print(answer)