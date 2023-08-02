X = int(input())

num = 1
while True:
    if num * (num + 1) / 2 >= X:
        break

    num += 1

if num % 2 == 0:
    top = X - (num * (num - 1) / 2)
    bot = num + 1 - top

else:
    bot = X - (num * (num - 1) / 2)
    top = num + 1 - bot



print(f"{int(top)}/{int(bot)}")