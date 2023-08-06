L = int(input())

answer = 0
hash_val = 1234567891

lst = list(input())

for i in range(L):
    num = ord(lst[i]) - ord('a') + 1
    answer += num * (31 ** i)
    answer %= hash_val

print(answer)
