hour, minute = map(int, input().split())

cook_time = int(input())

hour = hour + cook_time // 60
minute = minute + cook_time % 60

if minute >= 60:
    minute -= 60
    hour += 1

if hour >= 24:
    hour -= 24

print(hour, minute)