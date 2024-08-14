def solution(files):
    answer = []
    
    file_list = []
    
    file_idx = 0
    
    for file in files:
        
        head_idx = 0
        number_idx = 0
        
        for i in range(len(file)):
            if file[i].isdigit():
                head_idx = i
                break
        
        for i in range(head_idx, len(file)):
            if not file[i].isdigit():
                number_idx = i
                break
        if number_idx == 0:
            number_idx = len(file)
        
        tmp_head = file[:head_idx]
        tmp_number = file[head_idx:number_idx]
        
        print(tmp_head)
        print(tmp_number)
        file_list.append([tmp_head.upper(), int(tmp_number), file_idx])
        file_idx += 1
        
    
    print(file_list)
    
    file_list.sort(key=lambda x: (x[0], x[1], x[2]))
    
    print(file_list)
    
    for file in file_list:
        answer.append(files[file[2]])
    
    return answer