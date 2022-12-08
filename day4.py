data = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']
from util import parse_input

data = parse_input('data/day4.txt')
if data[-1] == '':
    data.pop(-1)

count = 0
for row in data:
    p1, p2 = row.split(',')
    p1_start, p1_end = p1.split('-')
    p2_start, p2_end = p2.split('-')

    p1_start, p1_end, p2_start, p2_end = int(p1_start), int(p1_end), int(p2_start), int(p2_end)

    flag = False
    if p2_start <= p1_start and p1_end <= p2_end:
        count += 1
        flag = True

    if p1_start <= p2_start and p2_end <= p1_end and not flag:
        count += 1

print(count)

count = 0
for row in data:
    p1, p2 = row.split(',')
    p1_start, p1_end = p1.split('-')
    p2_start, p2_end = p2.split('-')
    p1_start, p1_end, p2_start, p2_end = int(p1_start), int(p1_end), int(p2_start), int(p2_end)

    p1_list = [item for item in range(p1_start, p1_end+1)]
    p2_list = [item for item in range(p2_start, p2_end+1)]

    flag = False
    p1_flag = False
    p2_flag = False
    for item in p1_list:
        if item in p2_list:
            p1_flag = True
            flag = True

    for item in p2_list:
        if not flag and item in p1_list:
            p2_flag = True

    if p1_flag or p2_flag:
        count += 1

print(count)

