a = input()

b = a.replace('-', '+-')

lst = list(b.split('+'))

answer = 0
is_minus = 0
for item in lst:
    if int(item) < 0:
        is_minus = 1

    if is_minus:
        if int(item) > 0:
            answer -= int(item)
        else:
            answer += int(item)
    else:
        answer += int(item)

print(answer)
