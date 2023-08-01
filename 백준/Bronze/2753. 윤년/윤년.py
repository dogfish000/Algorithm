leap_year = int(input())
is_leap_year = False


if ((leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0):
    is_leap_year = True

print(int(is_leap_year))