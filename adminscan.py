import os
import re
import sys
import urllib
from urllib import request
import chardet
import requests
import time

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


def http_status(arg):
    # 虽然后期自己写了一下，还是很感谢CSDN的资料，以便于我这么快的学了requests。
    html = requests.get(arg)
    code = html.status_code
    # print(code)
    return code


#  后台扫描思路：
#    根据文档来循环判断网站状态
def adminscan_php(urls, delays):
    # 后台文件地址：config\admin_php.txt
    time.sleep(delays)  # 防止waf拦截
    for line in open("config\\admin_php.txt"):
        line = line.strip('\n')  # 去掉换行符
        black = urls + line
        codeings = http_status(black)
        if codeings == 200:
            print("可能存在后台：", black)
    pass


def adminscan_asp(urls, delays):
    # 后台文件地址：config\admin_asp.txt
    time.sleep(delays)  # 防止waf拦截
    for line in open("config\\admin_asp.txt"):
        line = line.strip('\n')  # 去掉换行符
        black = urls + line
        codeings = http_status(black)
        if codeings == 200:
            print("可能存在后台：", black)
    pass


def adminscan_aspx(urls, delays):
    # 后台文件地址：config\admin_aspx.txt
    time.sleep(delays)  # 防止waf拦截
    for line in open("config\\admin_aspx.txt"):
        line = line.strip('\n')  # 去掉换行符
        black = urls + line
        codeings = http_status(black)
        if codeings == 200:
            print("可能存在后台：", black)
    pass


def adminscan_jsp(urls, delays):
    # 后台文件地址：config\admin_jsp.txt
    time.sleep(delays)  # 防止waf拦截
    for line in open("config\\admin_jsp.txt"):
        line = line.strip('\n')  # 去掉换行符
        black = urls + line
        codeings = http_status(black)
        if codeings == 200:
            print("可能存在后台：", black)
    pass


def adminscan_dir(urls, delays):
    # 后台文件地址：config\admin_dir.txt
    time.sleep(delays)  # 防止waf拦截
    for line in open("config\\admin_dir.txt"):
        line = line.strip('\n')  # 去掉换行符
        black = urls + line
        codeings = http_status(black)
        if codeings == 200:
            print("可能存在后台：", black)
    pass


def adminscan_mdb(urls, delays):
    # 后台文件地址：config\admin_mdb.txt
    time.sleep(delays)  # 防止waf拦截
    for line in open("config\\admin_mdb.txt"):
        line = line.strip('\n')  # 去掉换行符
        black = urls + line
        codeings = http_status(black)
        if codeings == 200:
            print("可能存在后台：", black)
    pass


def adminscan_sql(urls, delays):
    # 后台文件地址：config\admin_sql.txt
    time.sleep(delays)  # 防止waf拦截
    for line in open("config\\admin_sql.txt"):
        line = line.strip('\n')  # 去掉换行符
        black = urls + line
        codeings = http_status(black)
        if codeings == 200:
            print("可能存在后台：", black)
    pass
