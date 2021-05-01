'''
main idea:
遍历每一个关联了issue 的pr
    看看这个pr是不是在收集的数据中心。获取stage，
    stage_1 += δtime
    number +=1
    ave = stage/num
'''

import xlrd

book = xlrd.open_workbook('bug_duration_time.xls')
sheet = book.sheets()[0]

book2 = xlrd.open_workbook('labeled_dataset.xlsx')
sheet2 = book2.sheets()[0]

all_bug_prs = {}
for line in range(sheet2.nrows-1):
    line = line + 1
    project = sheet2.cell_value(line, 0)
    pr_id = sheet2.cell_value(line, 1)
    pr_id = str(int(pr_id))
    stage = sheet2.cell_value(line, 9)
    stage = str(stage).strip()
    stage_id = 3
    if stage == 'Model Loading':
        stage_id = 0
    elif stage == 'High-Level IR Transformation':
        stage_id = 1
    elif stage == 'Low-Level IR Transformation':
        stage_id = 2
    else:
        continue

    all_bug_prs[f'{project}_{pr_id}'] = stage_id
#
# for key in all_bug_prs.keys():
#     print(key, all_bug_prs[key])

res = [[], [], []]

from datetime import datetime
for i in range(sheet.nrows-1):
    i = i + 1
    related_pr_id = sheet.cell_value(i, 1)
    open_time = sheet.cell_value(i, 2)
    close_time = sheet.cell_value(i, 3)
    project_name = sheet.cell_value(i, 4)
    related_pr_id = str(related_pr_id).split('/')[-1]

    open = datetime.strptime(open_time, "%Y-%m-%dT%H:%M:%SZ")
    close = datetime.strptime(close_time, "%Y-%m-%dT%H:%M:%SZ")
    duration = close - open
    assert duration.seconds >= 0, "duration less than 0"

    # print(duration.days, related_pr_id)
    pr_id_simple = f'{project_name}_{related_pr_id}'
    if pr_id_simple not in all_bug_prs.keys():
        continue

    res[all_bug_prs[pr_id_simple]].append(duration)
    print(all_bug_prs[pr_id_simple], duration.days, pr_id_simple)

for item in res:
    all_time = 0
    for time in item:
        time = time.days
        all_time += time
    print(all_time / len(item))
