pay_cost = int(input())
real_cost = 0

item_no = int(input())

for i in range(item_no):
    a, b = map(int, input().split())
    real_cost += (a * b)

if pay_cost == real_cost:
    print("Yes")
else:
    print("No")