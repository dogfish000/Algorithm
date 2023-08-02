A, B, V = map(int, input().split())

day = 1

height = V - A

if height % (A - B) == 0:
    day += height // (A - B)
else:
    day += 1
    day += height // (A - B)

print(day)


