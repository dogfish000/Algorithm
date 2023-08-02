def is_prime(number):
    if number == 1:
        return 0

    num = int(number ** 0.5)

    for i in range(2, num + 1):
        if number % i == 0:
            return 0

    return 1


N = int(input())

lst = list(map(int, input().split()))

prime_lst = []

for item in lst:
    prime_lst.append(is_prime(item))

print(sum(prime_lst))
