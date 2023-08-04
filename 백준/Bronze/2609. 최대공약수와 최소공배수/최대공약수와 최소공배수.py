def bp(a, b):
    if b == 0:
        return a

    a, b = b, a % b

    return bp(a, b)


num1, num2 = map(int, input().split())

print(bp(num1, num2))
print(int(num1 * num2 / bp(num1, num2)))