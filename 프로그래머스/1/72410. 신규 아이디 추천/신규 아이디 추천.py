def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    print(new_id)
    
    # 2단계
    tmp_new_id = ''
    for n in new_id:
        if ord('0') <= ord(n) <= ord('9') or ord('a') <= ord(n) <= ord('z') or ord(n) in [ord('-'), ord('_'), ord('.')]:
            tmp_new_id += n
    
    new_id = tmp_new_id
    print(new_id)
    
    # 3단계
    tmp_new_id = ''
    tmp_stack = []
    for n in new_id:
        if n == '.':
            tmp_stack.append('.')
        else:
            if tmp_stack:
                tmp_new_id += '.'
                tmp_stack.clear()
            tmp_new_id += n
    
    if tmp_stack:
        tmp_new_id += '.'
    
    new_id = tmp_new_id
    print(new_id)

    # 4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
        
    print(new_id)
    
    # 5단계
    if new_id == '':
        new_id = 'a'
    
    print(new_id)
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)
    
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
            
    print(new_id)
    
    answer = new_id
    
    return answer