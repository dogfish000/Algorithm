def solution(phone_book):
    answer = True
    
    len_book = len(phone_book) 
    phone_book.sort()
    
    for i in range(len_book - 1):
        len_tmp = len(phone_book[i])
        
        if phone_book[i] == phone_book[i + 1][:len_tmp]:
            answer = False
            break
    
    return answer