def solution(arr1, arr2):
    answer = [[]]
    
    arr_len_1 = len(arr1)
    arr_len_2 = len(arr1[0])
    answer = [[0] * arr_len_2 for _ in range(arr_len_1)]
    
    for i in range(arr_len_1):
        for j in range(arr_len_2):
            
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer