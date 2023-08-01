hour, minute = map(int, input().split())

if (minute < 45):
    minute = minute - 45 + 60

    if hour != 0:
        hour = hour - 1
    
    else:
        hour = 23

else:
    minute = minute - 45

print(hour, minute)