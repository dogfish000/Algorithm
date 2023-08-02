N, B = map(int, input().split())

answer = ''

while N > 0:
    num = N % B
    if num >= 10:
        num = chr(ord('A') + num - 10)

    answer = str(num) + answer

    N = N // B

print(answer)

