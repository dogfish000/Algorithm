def solution(bandage, health, attacks):
    answer = health
    
    time = attacks[-1][0]
    
    attack_dic = {}
    for attack in attacks:
        attack_dic[attack[0]] = attack[1]
        
    success = 0
    for i in range(1, time + 1):
        if i in attack_dic:
            answer = answer - attack_dic[i]
            if answer <= 0:
                answer = -1
                break
            success = 0
        else:
            success += 1
            answer += bandage[1]
            if answer > health:
                answer = health
        
        if success == bandage[0]:
            success = 0
            answer += bandage[2]
            if answer > health:
                answer = health
            
    
    
    
    
    return answer