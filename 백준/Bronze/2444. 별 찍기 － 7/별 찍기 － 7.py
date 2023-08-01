N = int(input())

for i in range(1, 2 * N):
    for _ in range(abs(N - i)):
        print(" ", end="")

    for _ in range(min(2 * i - 1, 2 * (2 * N - i) - 1)):
        print("*", end="")

    if i == 2 * N - 1:
        break

    print()
