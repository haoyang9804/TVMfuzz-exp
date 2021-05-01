'''
收集每个PR修改的代码行数，只要统计 ‘-’ 的LOC，因为这些代码在提交的时候被改动or删除了。
能够作为一个critical level。
'''


import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import xlwt
import os
import xlrd


def run(file_path):
    data = xlrd.open_workbook(file_path)
    table = data.sheets()[0]

    write_file = r'C:\Users\qingc\Desktop\rebuttal_material\submit\labeled_dataset2.xls'
    data2 = xlwt.Workbook(encoding='utf-8')
    table2 = data2.add_sheet("new_add")

    # res = []
    i = 0
    for line in range(table.nrows-1):
        line = line + 1
        link = table.cell_value(line, 3)
        sub_n, add_n = get_patch_line(link)
        print(sub_n, add_n)
        table2.write(line, 0, link)
        table2.write(line, 1, sub_n)
        table2.write(line, 2, add_n)

        # res.append(link)

    data2.save(write_file)
    return


def get_patch_line(link):
    sub_n = 0
    add_n = 0
    link = link + '/files'
    html = getHTML(link)
    soup = BeautifulSoup(html, "html.parser")
    lines_sub = soup.findAll(name="span", attrs={"class": "blob-code-inner blob-code-marker", "data-code-marker": '-'})
    lines_add = soup.findAll(name="span", attrs={"class": "blob-code-inner blob-code-marker", "data-code-marker": '+'})
    # print(len(lines_sub), len(lines_add))
    sub_n = len(lines_sub)
    add_n = len(lines_add)
    return sub_n, add_n


def getHTML(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        "Cookie": "_octo=GH1.1.1330774903.1574580347; _ga=GA1.2.448708474.1574580349; _device_id=31edb9dacd61bab06fb40eada4b9be59; user_session=hSr0DkrXUlMWrd7dvTQWd09ijHm9gmN6bNc_g_AvtWCyRh5P; __Host-user_session_same_site=hSr0DkrXUlMWrd7dvTQWd09ijHm9gmN6bNc_g_AvtWCyRh5P; dotcom_user=jikechao; tz=Asia%2FTaipei; logged_in=yes; has_recent_activity=1; _gh_sess=%2Ba%2BuPRxMED1RMpWxe1Sn3%2FmkOSGeVU9dxFtjfz%2Fxba3ah32x6PkuaXEOeuqxqoOzeTSrIyS6B%2Fv8fbwsQWnGUX9eLiuoJqZNB2O0MgJRNDWg6iAcEqHjqq6jTMfW27y4f5ajnhGhEpayrsWZE2cpVXihPcxqKPHGFdmbvGpsRtAef2ul8T2Av2Z2nW0q0aGzJBx9Bk%2F%2Brjdr727RO1qGkuxjIz7G2DBaygs8Q5zRmVbbCxlnc9KDo6JEutQQmAIzvmSFvORxf%2BdrQGcx1ONHQAnz8jWjzVfYqRGhfCBD%2B4E5KD81J8oT0DCnnhsoEAAoV0ABGYai7UtWU%2B0l2vWJeLQ%2ByortIdZmqoF3T6sFxGs%3D--NrbieUGB2S7OoTLb--QXYppKqLl5BHS%2BtQw0sofA%3D%3D"
    }
    try:
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        return html
    except Exception as e:
        print("exception", e)
        import time
        time.sleep(2)


if __name__ == '__main__':
    file_path = r'C:\Users\qingc\Desktop\rebuttal_material\submit\labeled_dataset.xlsx'
    pr_links = run(file_path)



