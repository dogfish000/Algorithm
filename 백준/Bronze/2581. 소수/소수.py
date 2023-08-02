def is_prime(number):
    if number == 1:
        return 0

    num = int(number ** 0.5)

    for i in range(2, num + 1):
        if number % i == 0:
            return 0

    return number


N = int(input())

M = int(input())

prime_lst = []
for i in range(N, M + 1):
    if is_prime(i):
        prime_lst.append(is_prime(i))

if len(prime_lst) == 0:
    print(-1)
else:
    print(sum(prime_lst))
    print(min(prime_lst))
