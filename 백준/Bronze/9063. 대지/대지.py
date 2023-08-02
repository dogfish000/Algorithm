N = int(input())

lst_x = []
lst_y = []

for _ in range(N):
    x, y = map(int, input().split())
    lst_x.append(x)
    lst_y.append(y)
    
length = max(lst_x) - min(lst_x)
height = max(lst_y) - min(lst_y)

area = length * height

print(area)