def solution(numbers):
    answer = 0
    prime_list = []
    
    numbers = list(numbers)
    visited = [0] * len(numbers)
    
    
    
    def find_prime(cur_num):
        if cur_num != '':
            cur_num = int(cur_num)
            if is_prime(cur_num) and cur_num not in prime_list:
                prime_list.append(cur_num)
            cur_num = str(cur_num)
    
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = 1
                find_prime(cur_num + numbers[i])
                visited[i] = 0
    
    
    def is_prime(n):
        if n <= 1:
            return False
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    find_prime('')
    
    answer = len(prime_list)
    
    
    return answer