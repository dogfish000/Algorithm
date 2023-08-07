N = int(input())

member = {}

for _ in range(N):
    age, name = input().split()
    age = int(age)

    if age in member:
        member[age].append(name)

    else:
        member[age] = [name]

lst = list(member.keys())

lst.sort()

for age in lst:
    for n in member[age]:
        print(age, n)