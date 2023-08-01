my_set = set()

for _ in range(10):
    my_set.add(int(input()) % 42)

print(len(my_set))