def solution(friends, gifts):
    answer = 0
    
    fr_dic = {}
    pr_dic = {}
    
    idx = 0
    for friend in friends:
        pr_dic[friend] = 0
        fr_dic[friend] = idx
        idx += 1
    
    N = len(friends)
    
    lst = [[0] * N for _ in range(N)]
    
    for gift in gifts:
        fr, to = gift.split()
        lst[fr_dic[fr]][fr_dic[to]] += 1
        
    
    for i in range(N):
        for j in range(i + 1, N):
            if i == j:
                continue
            
            if lst[i][j] > lst[j][i]:
                pr_dic[friends[i]] += 1
            elif lst[j][i] > lst[i][j]:
                pr_dic[friends[j]] += 1
            else:
                a = sum(lst[i])
                b = sum(lst[j])
                for k in range(N):
                    a -= (lst[k][i])
                    b -= (lst[k][j])
                
                if a > b:
                    pr_dic[friends[i]] += 1
                elif a < b:
                    pr_dic[friends[j]] += 1
                    
    
    answer = max(pr_dic.values())
                
            
            
            
            
    
    return answer