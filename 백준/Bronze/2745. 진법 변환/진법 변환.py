N, B = input().split()

total = 0

for i in range(len(N) - 1, -1, -1):
    if N[i].isdigit():
        total += int(N[i]) * (int(B) ** (len(N) - 1 - i))
    else:
        total += (10 + ord(N[i]) - ord('A')) * (int(B) ** (len(N) - 1 - i))

print(total)
