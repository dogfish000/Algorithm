def solution(nums):
    answer = 0
    s = set()
    for num in nums:
        s.add(num)
        
    answer = min(len(s), len(nums) / 2)
    return answer