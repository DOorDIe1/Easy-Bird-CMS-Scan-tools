"""
Copyright (c) 2020-2021 Moxin
   [Software Name] is licensed under Mulan PSL v2.
   You can use this software according to the terms and conditions of the Mulan PSL v2.
   You may obtain a copy of Mulan PSL v2 at:
            http://license.coscl.org.cn/MulanPSL2
   THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
   See the Mulan PSL v2 for more details.
By：M0x1n Time：2020.12.23Updated
Ver:1.2(Third edition) 1.2第三版
https://bbs.moxinwangluo.cn/
此脚本可以通过一些网站特征来进行CMS识别，当然，这个脚本也是开源的。
This script can be used for CMS recognition based on some website features, and of course, this script is also open source.
"""
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
    f = open("date\\web.txt", encoding=http_type(url))
    line = f.read()
    if keyLine in line:
        f.close()
        return "Pass"
    else:
        f.close()
        return "Failed"
    pass


def searchrobots(keyLine, url):  # 新版本更改了缓存地址 D:2020年12月24日16:59:19
    # searchLine代码来自：https://www.cnblogs.com/Amy20182018/articles/8962013.html
    f = open("date\\robots.txt", encoding=http_type(url))
    line = f.read()
    if keyLine in line:
        f.close()
        return "Pass"
    else:
        f.close()
        return "Failed"
    pass
