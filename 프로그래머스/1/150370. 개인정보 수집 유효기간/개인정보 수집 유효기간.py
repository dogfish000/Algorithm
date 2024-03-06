def solution(today, terms, privacies):
    answer = []
    
    dic = {}
    for term in terms:
        a, b = term.split()
        dic[a] = int(b)
        
    td_date = 0
    today_y, today_m, today_d = today.split('.')
    today_y, today_m, today_d = int(today_y), int(today_m), int(today_d)
    td_date = int(today_y) * 10000 + int(today_m) * 100 + int(today_d)
        
    for i in range(len(privacies)):
        td = privacies[i]
        date, valid_month = td.split()
        y, m, d = date.split('.')
        y, m ,d = int(y), int(m), int(d)
        print(date, valid_month)
        tmp = dic[valid_month]
        print(tmp)
        
        y = y + (tmp // 12)
        m = m + (tmp % 12)
        
        if m > 12:
            m = m - 12
            y = y + 1
            
            
        if y*10000 + m *100 + d <= td_date:
            answer.append(i + 1)
        
        
    print(dic)
    
    
    
    return answer