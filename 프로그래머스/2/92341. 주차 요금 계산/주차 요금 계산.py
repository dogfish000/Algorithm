import math

def solution(fees, records):
    answer = []
    
    park_dic = {}
    time_dic = {}
    fee_list = []
    
    
    for record in records:
        record_lst = list(record.split())
        
        time = list(map(int, record_lst[0].split(':')))
        
        park_time = time[0] * 60 + time[1]
        
        if record_lst[2] == "IN":
            park_dic[record_lst[1]] = park_time
        
        if record_lst[2] == "OUT":
            tmp_time = park_time - park_dic[record_lst[1]]
            park_dic.pop(record_lst[1])
            if record_lst[1] in time_dic:
                time_dic[record_lst[1]] += tmp_time
            else:
                time_dic[record_lst[1]] = tmp_time
    
            
    
    if park_dic:
        for k,v in park_dic.items():
            tmp_time = (23*60 + 59) - v
            if k in time_dic:
                time_dic[k] += tmp_time
            else:
                time_dic[k] = tmp_time
    
                     
    print(time_dic)
    
    for k,v in time_dic.items():
        tmp_fee = fees[1]
        if v > fees[0]:
            tmp_fee = tmp_fee + math.ceil((v - fees[0]) / fees[2]) * fees[3] 
        fee_list.append([k, tmp_fee])
    
    print(fee_list)
    fee_list.sort(key=lambda x: x[0])
    print(fee_list)
    
    for f in fee_list:
        answer.append(f[1])
    
    
    
    return answer