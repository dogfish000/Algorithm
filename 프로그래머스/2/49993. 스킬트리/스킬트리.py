def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        tmp = []
        for sk in skill_tree:
            if sk in skill and sk not in tmp:
                tmp.append(sk)
        
        a = ''.join(tmp)
        
        if skill[:len(a)] == a:
            answer += 1
    
    

    
    
        
    
    
    
    
    return answer