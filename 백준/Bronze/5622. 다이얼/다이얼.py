S = input()
total = 0
for s in S:
    if ord(s) <= ord('S'):
        time = 2 + ((ord(s) % 62) // 3)
        if s == 'S':
            time -= 1
        total += time
    else:
        time = 2 + ((ord(s) % 63) // 3)
        if s == 'Z':
            time -= 1
        total += time


print(total)