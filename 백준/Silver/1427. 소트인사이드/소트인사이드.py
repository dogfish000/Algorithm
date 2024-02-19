lst = list(map(int, input()))

lst.sort(reverse=True)

ans = 0
for i in range(len(lst)):
    ans += lst[i]
    if i == (len(lst) - 1):
        break
    ans *= 10

print(ans)