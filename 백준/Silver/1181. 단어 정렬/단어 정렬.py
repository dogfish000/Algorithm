my_dict = {}

N = int(input())

for _ in range(N):
    value = input()
    key = len(value)
    if key in my_dict:
        my_dict[key].append(value)
    else:
        my_dict[key] = [value]


key_lst = list(my_dict.keys())

key_lst.sort()

for key in key_lst:
    tmp_lst = list(set(my_dict[key]))
    tmp_lst.sort()

    for tmp in tmp_lst:
        print(tmp)




