def solution(arr1, arr2):
    
    answer = []
    
    N = len(arr1)
    M = len(arr1[0])
    L = len(arr2[0])
    
    for i in range(N):
        tmp_lst = []
        for j in range(L):
            tmp = 0
            for k in range(M):
                tmp += arr1[i][k] * arr2[k][j]
            tmp_lst.append(tmp)
        answer.append(tmp_lst)
                
            
            
    
    
    
    return answer