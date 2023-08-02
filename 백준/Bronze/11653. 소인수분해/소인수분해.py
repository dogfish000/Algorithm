N = int(input())
lst = []

while True:
    for i in range(2, N + 1):
        if N % i == 0:
            lst.append(i)
            N = N // i
            break
    if N == 1:
        break

lst.sort()

for item in lst:
    print(item)