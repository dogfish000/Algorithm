N = int(input())


for i in range(1, N + 1):
    a = ("*" * i)
    print(a.rjust(N))
    