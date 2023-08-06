L = int(input())

answer = 0

lst = list(input())

for i in range(L):
    num = ord(lst[i]) - ord('a') + 1
    answer += num * (31 ** i)

print(answer)
