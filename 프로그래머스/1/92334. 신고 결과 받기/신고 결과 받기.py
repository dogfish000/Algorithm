def solution(id_list, report, k):
    answer = []
    
    report_dic = {}
    
    for repo in report:
        a, b = repo.split()
        
        if b not in report_dic.get(a, []):
            report_dic[a] = report_dic.get(a, []) + [b]
        
    
    count_dic = {}
    for value in report_dic.values():
        for v in value:
            count_dic[v] = count_dic.get(v, 0) + 1
            
    print(count_dic)
    
    for f in id_list:
        tmp = 0
        if f in report_dic:
            for t in report_dic[f]:
                if t in count_dic and count_dic[t] >= k:
                    tmp += 1
                
        answer.append(tmp)
                
    
    return answer