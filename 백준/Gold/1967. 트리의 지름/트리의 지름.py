import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

if N != 1:
    dic = {}
    
    for _ in range(N - 1):
        s, e, k = map(int, input().split())
        dic[s] = dic.get(s, []) + [[e, k]]
        dic[e] = dic.get(e, []) + [[s, k]]
    
    
    def find_length(start):
        dp[start] = 0
    
        q = deque()
        q.append(start)
        while q:
            v = q.popleft()
            if v in dic:
                for item in dic[v]:
                    nv, nk = item[0], item[1]
                    if dp[nv] > dp[v] + nk:
                        dp[nv] = dp[v] + nk
                        q.append(nv)
    
    dp = [987654321] * (N + 1)
    dp[0] = 0
    find_length(1)
    
    idx = dp.index(max(dp))
    
    dp = [987654321] * (N + 1)
    dp[0] = 0
    find_length(idx)
    
    answer = max(dp)
    print(answer)
    
else:
    print(0)
