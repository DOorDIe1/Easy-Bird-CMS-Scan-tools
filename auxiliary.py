import os
import re
import sys
import urllib
from urllib import request
import chardet
import requests


# 查找文本


def http_status(arg):
    # 虽然后期自己写了一下，还是很感谢CSDN的资料，以便于我这么快的学了requests。
    html = requests.get(arg)
    code = html.status_code
    # print(code)
    return code


def http_type(url):
    """
    这是之前来源于CSDN的资料，最后自己还是用requset写出来了
    #https://blog.csdn.net/github_34605078/article/details/52027156
    #https://blog.csdn.net/IMW_MG/article/details/78783691?utm_source=blogxgwz4&utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-2&spm=1001.2101.3001.4242
    data1 = urllib.request.urlopen(urllib.request.Request(url)).read()
    chardit1 = chardet.detect(data1)
    if chardit1['encoding'] == "utf-8" or chardit1['encoding'] == "UTF-8":
        return "UTF-8"
    else:
        return "GBK"
    """
    html = requests.get(url)
    return html.encoding


def searchLine(keyLine, url):
    # searchLine代码来自：https://www.cnblogs.com/Amy20182018/articles/8962013.html
    f = open("web.txt", encoding=http_type(url))
    line = f.read()
    if keyLine in line:
        f.close()
        return "Pass"
    else:
        f.close()
        return "Failed"
    pass



