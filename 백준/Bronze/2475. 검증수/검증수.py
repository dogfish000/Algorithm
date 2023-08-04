lst = list(map(int, input().split()))


total = 0
for item in lst:
    total += item ** 2

print(total % 10)