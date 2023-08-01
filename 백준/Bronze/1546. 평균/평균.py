N = int(input())

num_lst = list(map(int, input().split()))   

max_value = max(num_lst)

for i in range(len(num_lst)):
    num_lst[i] = num_lst[i] / max_value * 100

avg = sum(num_lst) / len(num_lst)

print(avg)
