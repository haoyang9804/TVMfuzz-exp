import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import xlwt
import os

base_pr_url = r"https://github.com/"

'''
github issue have a limit url length ,the max keys is 5(in this search),
 so we run 2 time with different keywords to collect all bug and then merged them
'''
keywords_all = ["fix", "bug", "error", "issue", "correct", 'defect', 'mistake', 'fault', 'flaw']
keywords = ["fix", "bug", "error", "issue", "correct"]
keywords2 = ['defect', 'mistake', 'fault', 'flaw']


def getBaseUrl(project, page, from_label):
    url = "https://github.com/" + project + "/issues?page=" + str(page)
    if from_label:
        if 'tvm' in project:
            url_latter = r'&q=label%3A"type%3A+bug"+is%3Amerged'
        else:
            url_latter = r"&q=is%3Amerged+label%3ABug"

    else:
        url_latter = r"&q=is%3Amerged"
        url_latter += "+" + keywords[0] + "+in%3Atitle"
        for i in range(len(keywords)-1):
            url_latter += "+OR+" + keywords[i+1] + "+in%3Atitle"
    url += url_latter
    # url += r"+sort%3Acreated-desc"   # sort by create
    print(url)
    return url


def getFragementFiles(url):
    files_string = ""
    html = getHTML(url)
    soup = BeautifulSoup(html, "html.parser")

    files_sub = soup.findAll("div", id=re.compile("^diff-[\d|a-f]"))
    files_sub_num = len(files_sub)
    print("files_sub_num", files_sub_num)
    for file_sub in files_sub:
        file_sub_name = file_sub.find("a", href=re.compile("^#diff-")).text
        files_string = files_string + file_sub_name + "\n"
    return files_string


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


def get_pr_files(html):
    res_string = ""

    soup = BeautifulSoup(html, "html.parser")
    files_num_true = soup.find("span", id="files_tab_counter").string

    files = soup.findAll("div", id = re.compile("^diff-"))
    files_num = len(files)

    for file in files:
        file_name = file.find("a", href=re.compile("^#diff-"))
        # print(file_name.text)
        if file_name is None:
            print("debug:---file_name is not exist!!", file_name)
        else:
            res_string += file_name.text + "\n"

    if files_num_true != str(files_num):
        fragment = soup.findAll("include-fragment", src=re.compile("diffs?"))[0]
        fragment_url = "https://github.com/" + fragment.get("src")
        print(fragment_url)
        res_string_sub = getFragementFiles(fragment_url)
        res_string += res_string_sub

    return files_num_true, res_string


def entry(project, from_label=False):
    book = xlwt.Workbook(encoding='utf-8')
    if not from_label:
        sheet = book.add_sheet(project.split('/')[1])
    else:
        sheet = book.add_sheet(project.split('/')[1] + "_label")

    page = 1
    while True:
        print("page:", page)
        url = getBaseUrl(project, page, from_label)
        html = getHTML(url)
        soup = BeautifulSoup(html, "html.parser")

        issues_div = soup.findAll("div", id=re.compile(r"issue_\d+"))
        for i in range(len(issues_div)):
            try:
                pr_id = issues_div[i]['id'].split('_')[1]
                title = issues_div[i].findAll("a", id="issue_" + pr_id + '_link')[0].string.strip()
                time = issues_div[i].findAll("relative-time")[0]["datetime"].split("T")[0]
                # print(title, pr_id, time ,sep="\t")
                comments_links = issues_div[i].findAll("a")

                comments_num = 0
                for link in comments_links:
                    if link.has_attr("aria-label") and "comment" in link["aria-label"]:
                        # print("debug:----link is", link)
                        comments_num = link["aria-label"].split(" ")[0]
                        break

                #  open every single bug link, collect pull files
                url_single_bug = base_pr_url + project + "/pull/" + pr_id
                url_single_bug_files = url_single_bug + "/files"
                print(url_single_bug)

                html_single_bug = getHTML(url_single_bug_files)
                files_num_true, files_string = get_pr_files(html_single_bug)

                print("comments_num", comments_num)
                print(files_num_true, files_string)
                print("-------------------------------------------------------------------------")

                sheet.write((page-1)* 25 + i, 0, pr_id)
                sheet.write((page-1)*25 + i, 1, title)
                sheet.write((page-1)*25 + i, 2, url_single_bug)
                sheet.write((page - 1) * 25 + i,3, time)
                sheet.write((page-1) * 25 + i, 4, comments_num)
                sheet.write((page-1)* 25 +i, 5, files_string)
                sheet.write((page-1)*25 +i, 6, files_num_true)

            except Exception as e:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(e, url_single_bug)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                continue
        if len(issues_div) < 25:    # last page may be not contain total 25 bugs
            print("finish all! ")
            break
        # if page == 1:
        #     break
        page = page + 1
        print("finish page:", page-1, "")
    if from_label:
        book.save("../result/bug_github_" + project.split("/")[1] + "_labels" + ".xls")
    else:
        book.save("../result/bug_github_"+project.split("/")[1]+".xls")
    return


if __name__ == '__main__':
    if not os.path.exists("../result"):
        os.makedirs("../result/")

    projects = ["apache/tvm", "pytorch/glow", "NervanaSystems/ngraph-onnx", "NervanaSystems/ngraph-mxnet", "NervanaSystems/ngraph-tf"]
    for project in projects:
        entry(project, from_label=True)
        entry(project, from_label=False)
