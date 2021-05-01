
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import xlwt
import os
import xlrd

book = xlwt.Workbook(encoding='utf-8')
table = book.add_sheet("bugfix_time")
n_line = 0


def run(project):
    page = 1
    while True:
        url = f'https://github.com/{project}/issues?page={page}&q=is%3Aissue+is%3Aclosed'
        print(url)
        html = getHTML(url)
        soup = BeautifulSoup(html, 'html.parser')
        issues_div = soup.findAll("div", id=re.compile(r"issue_\d+"))
        for i in range(len(issues_div)):
            try:
                global n_line
                related_pr = issues_div[i].findAll(name="span", attrs={"aria-label": "1 linked pull request"})
                if len(related_pr) == 0:
                    continue
                issue_id = issues_div[i]['id'].split('_')[1]
                closed_time = issues_div[i].findAll("relative-time")[0]["datetime"]
                res = calc_duration(issue_id, project)
                if res is None:
                    continue
                pr_id, open_time = res
                print(issue_id, pr_id, open_time, closed_time)
                n_line = n_line + 1
                # print(n_line)
                table.write(n_line, 0, issue_id)
                table.write(n_line, 1, pr_id)
                table.write(n_line, 2, open_time)
                table.write(n_line, 3, closed_time)
            except Exception as e:
                print(e)
        if len(issues_div) < 25:    # last page may be not contain total 25 bugs
            print("finish all! ")
            break
        page = page + 1
        # break
    return


def calc_duration(issue_id, project):
    url = f'https://github.com/{project}/pull/{issue_id}'
    print(f"visit {url}")
    html = getHTML(url)
    soup = BeautifulSoup(html, "html.parser")
    open_info = open_time = soup.findAll(name='div', attrs={"class": "d-flex flex-items-center flex-wrap mt-0 gh-header-meta"})
    assert len(open_info) == 1, "wrong in get open time info!"

    open_time = open_info[0].findAll(name='relative-time')[0].get("datetime")
    # 在侧边栏中Linked PRs中获得pr_id
    pr_info = soup.findAll(name='div', attrs={"class": "css-truncate my-1"})
    assert len(pr_info) == 1, "pr link more than one"
    pr_id = pr_info[0].findAll(name='a')[0].get('href')
    return (pr_id, open_time)

    # pr_info = soup.findAll(name='div', attrs={"class": re.compile("mt-2 d-flex flex-items-start.*")})
    # if len(pr_info) == 0:
    #     print("no related pr")
    #     return None
    # for item in pr_info:
    #     pr_id = item.findAll(name='a')[0].get("href")
    #     if 'issues' in pr_id:
    #         continue
    #     # print(pr_id, open_time)
    #     return (pr_id, open_time)




def getHTML(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        # "Cookie": "_octo=GH1.1.1330774903.1574580347; _ga=GA1.2.448708474.1574580349; _device_id=31edb9dacd61bab06fb40eada4b9be59; user_session=hSr0DkrXUlMWrd7dvTQWd09ijHm9gmN6bNc_g_AvtWCyRh5P; __Host-user_session_same_site=hSr0DkrXUlMWrd7dvTQWd09ijHm9gmN6bNc_g_AvtWCyRh5P; dotcom_user=jikechao; tz=Asia%2FTaipei; logged_in=yes; has_recent_activity=1; _gh_sess=%2Ba%2BuPRxMED1RMpWxe1Sn3%2FmkOSGeVU9dxFtjfz%2Fxba3ah32x6PkuaXEOeuqxqoOzeTSrIyS6B%2Fv8fbwsQWnGUX9eLiuoJqZNB2O0MgJRNDWg6iAcEqHjqq6jTMfW27y4f5ajnhGhEpayrsWZE2cpVXihPcxqKPHGFdmbvGpsRtAef2ul8T2Av2Z2nW0q0aGzJBx9Bk%2F%2Brjdr727RO1qGkuxjIz7G2DBaygs8Q5zRmVbbCxlnc9KDo6JEutQQmAIzvmSFvORxf%2BdrQGcx1ONHQAnz8jWjzVfYqRGhfCBD%2B4E5KD81J8oT0DCnnhsoEAAoV0ABGYai7UtWU%2B0l2vWJeLQ%2ByortIdZmqoF3T6sFxGs%3D--NrbieUGB2S7OoTLb--QXYppKqLl5BHS%2BtQw0sofA%3D%3D"
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
    projects = ["apache/tvm", "pytorch/glow", "NervanaSystems/ngraph",
                "NervanaSystems/ngraph-onnx", "NervanaSystems/ngraph-mxnet", "NervanaSystems/ngraph-tf"]
    try:
        for project in projects:
            run(project)
    except Exception as e:
        print(e)
    finally:
        book.save(f"bug_duration_time.xls")
    book.save(f"bug_duration_time.xls")
