from auxiliary import http_status
import os
import auxiliary
import re
import sys
import urllib
from urllib import request
import chardet
import requests
import cms
import robotsscan


def dedever(url):
    if http_status(url + "data/admin/ver.txt") == 200:
        page = request.urlopen(url + "data/admin/ver.txt")
        content = page.read()
        fp = open("web.txt", "w+b")  # 打开一个文本文件
        fp.write(content)  # 写入数据
        fp.close()  # 关闭文件
        print("这个站点可能是织梦Dedecms，版本号：", content)
