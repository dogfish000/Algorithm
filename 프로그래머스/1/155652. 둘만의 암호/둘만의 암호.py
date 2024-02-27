def solution(s, skip, index):
    answer = ''
    # print(ord('a'), ord('z'))
    # 97, 122 
    
    skip_lst = []
    for sk in skip:
        skip_lst.append(ord(sk))
    print(skip_lst)
    
    for word in s:
        word_ord = ord(word)
        for i in range(index):
            word_ord += 1
            if word_ord > 122:
                word_ord = word_ord - 123 + 97
            while word_ord in skip_lst:
                word_ord += 1
                if word_ord > 122:
                    word_ord = word_ord - 123 + 97
                    
        answer += chr(word_ord)
                
            
    
    
    
    
    return answer