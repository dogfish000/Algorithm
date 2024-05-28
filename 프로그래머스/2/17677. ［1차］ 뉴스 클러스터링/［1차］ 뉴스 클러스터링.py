def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
   
    idx_a = ord('a')
    idx_z = ord('z')
    
    
    lst_str1 = []
    lst_str2 = []
    
    
    for i in range(len(str1) - 1):
        if idx_a <= ord(str1[i]) <= idx_z and idx_a <= ord(str1[i + 1]) <= idx_z:
            lst_str1.append(str1[i: i+2])
            
    for i in range(len(str2) - 1):
        if idx_a <= ord(str2[i]) <= idx_z and idx_a <= ord(str2[i + 1]) <= idx_z:
            lst_str2.append(str2[i: i+2])
    
   
    
    if len(lst_str1) == 0 :
        if len(lst_str2) == 0:
            return 65536
        else:
            return 0
        
    if len(lst_str2) == 0:
        return 0
    
    set_str1 = set(lst_str1)
    set_str2 = set(lst_str2)
    
    set_and = set_str1 & set_str2
    set_or = set_str1 | set_str2
    
    
    cnt_and = 0
    cnt_or = 0
    
    for num in set_and:
        cnt_and += min(lst_str1.count(num), lst_str2.count(num))
        
    for num in set_or:
        cnt_or += max(lst_str1.count(num), lst_str2.count(num))
    
    
    
    
    answer = int(65536 * cnt_and / cnt_or)
    
    
    return answer