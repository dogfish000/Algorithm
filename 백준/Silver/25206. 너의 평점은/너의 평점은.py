gpa_lst = []

for i in range(20):
    lst = list(input().split())
    gpa_lst.append(lst)

cnt_lecture = 0
gpa_sum = 0

gpa_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

for gpa in gpa_lst:
    if gpa[2] != 'P':
        cnt_lecture += float(gpa[1])
        gpa_sum += float(gpa[1]) * float(gpa_dict[gpa[2]])

print(gpa_sum / cnt_lecture)

