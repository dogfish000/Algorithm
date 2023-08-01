num1 = input()
num2 = input()


num3 = int(num1) * int(num2[2])
num4 = int(num1) * int(num2[1])
num5 = int(num1) * int(num2[0])

num6 = num3 + num4 * 10 + num5 * 100


for i in range(3, 7):
 

    print(f"{globals()['num'+str(i)]}")
