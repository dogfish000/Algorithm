lst = list(map(int, input().split()))

answer = ''

if lst == [1, 2, 3, 4, 5, 6, 7, 8]:
    answer = "ascending"
elif lst == [8, 7, 6, 5, 4, 3, 2, 1]:
    answer = "descending"
else:
    answer = "mixed"

print(answer)
