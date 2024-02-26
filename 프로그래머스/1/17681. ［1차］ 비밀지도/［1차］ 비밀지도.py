def solution(n, arr1, arr2):
    answer = []
    
    bin_arr1 = []
    bin_arr2 = []
    
    for item in arr1:
        bin_arr1.append(bin(item)[2:].zfill(n))
    
    for item in arr2:
        bin_arr2.append(bin(item)[2:].zfill(n))
        
        
    print(bin_arr1)
    print(bin_arr2)
    
    
    for i in range(n):
        tmp = ''
        for j in range(n):
            if bin_arr1[i][j] == '0' and bin_arr2[i][j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        
        answer.append(tmp)
                
        
    
    
    
    return answer