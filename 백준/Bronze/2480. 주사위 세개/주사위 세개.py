a, b, c = map(int, input().split())

prize_money = 0

if (a == b == c):
    prize_money = 10000 + a * 1000

elif (a == b != c):
    prize_money = 1000 + a * 100

elif (a == c != b):
    prize_money = 1000 + a * 100

elif (b == c != a):
    prize_money = 1000 + b * 100

else:
    prize_money = max(a, b, c) * 100


print(prize_money)