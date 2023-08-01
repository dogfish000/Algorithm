A, B = input().split()

a = A[::-1]
b = B[::-1]

answer = 0

if int(a) > int(b):
    answer = int(a)
else:
    answer = int(b)

print(answer)
