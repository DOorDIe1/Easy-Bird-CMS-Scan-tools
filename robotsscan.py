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
import auxiliary
import files
import os

def discuzrobots(url):
    if auxiliary.searchrobots('Discuz! X3', url) == "Pass":
        print("从robots.txt检测中得到", url, "可能是Discuz X3站点！")
    if auxiliary.searchrobots('/uc_server/', url) == "Pass":
        print("从robots.txt检测中得到", url, "可能是Discuz X3站点！（存在uc_server）")
    pass


def dederobots(url, uurl):
    if auxiliary.searchrobots('/plus/feedback_js.php', url) == "Pass":
        print("从robots.txt检测中得到", url, "可能是dedecms站点！")
        files.dedever(uurl)  # 下同，只有符合条件才会进行文件判断
    if auxiliary.searchrobots('/plus/shops_buyaction.php', url) == "Pass":
        print("从robots.txt检测中得到", url, "可能是dedecms站点！")
        files.dedever(uurl)
    pass


def allrobots(url, uurl):
    discuzrobots(url)
    dederobots(url, uurl)
    os.rmove("date\\robots.txt")
    pass
