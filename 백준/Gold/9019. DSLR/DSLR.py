T = int(input())
from collections import deque


for tc in range(1, T + 1):
    a, b = input().split()
    zero_a = a.zfill(4)
    zero_b = b.zfill(4)
    visited = [''] * 10000
    answer = ''

    def bfs(zero_a, zero_b, visited):
        queue = deque()
        queue.append(zero_a)
        visited[int(zero_a)] = ''

        while queue:
            v = queue.popleft()
            visit_val = visited[int(v)]
            if v == zero_b:
                global answer
                answer = visited[int(v)]
                break

            else:
                l_num = v[1:4] + v[0:1]
                r_num = v[3:4] + v[0:3]
                d_num = str((int(v) * 2) % 10000).zfill(4)
                if int(v) == 0:
                    s_num = '9999'
                else:
                    s_num = str(int(v) - 1).zfill(4)

                if visited[int(l_num)] == '':
                    queue.append(l_num)
                    visited[int(l_num)] = visit_val + 'L'
                if visited[int(r_num)] == '':
                    queue.append(r_num)
                    visited[int(r_num)] = visit_val + 'R'
                if visited[int(d_num)] == '':
                    queue.append(d_num)
                    visited[int(d_num)] = visit_val + 'D'
                if visited[int(s_num)] == '':
                    queue.append(s_num)
                    visited[int(s_num)] = visit_val + 'S'


    bfs(zero_a, zero_b, visited)

    print(answer)




