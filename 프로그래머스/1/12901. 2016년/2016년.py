def solution(a, b):
    answer = ''
    
    days_lst = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    day = 0 
    
    for i in range(1, a):
        day += days_lst[i]
    
    day += b
    print(day)
    print(day % 7)
    
    answer = date[day % 7]
    return answer