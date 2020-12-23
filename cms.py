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


def discuz(url):
    # 检测Discuz! X3.4
    if auxiliary.searchLine('Discuz! X3.4', url) == "Pass" or auxiliary.searchLine('Discuz!</a></strong> <em>X3.4',
                                                                                   url) == "Pass":
        {
            print("您扫描的网站" + url + "可能是Discuz！X3.4")
        }
    if auxiliary.searchLine('Discuz! X3.3', url) == "Pass" or auxiliary.searchLine('Discuz!</a></strong> <em>X3.3',
                                                                                   url) == "Pass":
        {
            print("您扫描的网站" + url + "可能是Discuz！X3.3")

        }
    if auxiliary.searchLine('Discuz! X3.2', url) == "Pass" or auxiliary.searchLine('Discuz!</a></strong> <em>X3.2',
                                                                                   url) == "Pass":
        {
            print("您扫描的网站" + url + "可能是Discuz！X3.2")
        }
    if auxiliary.searchLine('Discuz! X3.2', url) == "Pass" or auxiliary.searchLine('Discuz!</a></strong> <em>X3.2',
                                                                                   url) == "Pass":
        {
            print("您扫描的网站" + url + "可能是Discuz！X3.2")
        }
    elif auxiliary.searchLine('Discuz!', url) == "Pass":
        {
            print("您扫描的网站" + url + "可能是Discuz！的其他版本/修改版本！")
        }
    else:
        {
            print("站点可能不是Discuz哦~")
        }
    pass


def Z_Blog(url):
    # 检测Z-BlogPHP
    if auxiliary.searchLine('Z-BlogPHP', url) == "Pass":
        {
            print("您扫描的网站" + url + "是Z-BlogPHP")
        }
    if auxiliary.searchLine('Z-BlogASP', url) == "Pass":
        {
            print("您扫描的网站" + url + "是Z-BlogASP")
        }
    if auxiliary.searchLine('Powered By Z-Blog', url) == "Pass":
        {
            print("您扫描的网站" + url + "技术支持来自Z-Blog")
        }
    if auxiliary.searchLine('Z-Blog', url) == "Pass":
        {
            print("您扫描的网站" + url + "可能是/关于Z-Blog")
        }
    else:
        {
            print("站点可能不是Z-Blog哦~")
        }
    pass


def WordPress(url):
    if auxiliary.searchLine('WordPress 5.3.6', url) == "Pass":
        {
            print("您扫描的网站" + url + "是WordPress 5.3.6")
        }
    else:
        {
            print("站点可能不是WordPress哦~")
        }
    pass


def dedecms(url):
    if auxiliary.searchLine('href="/css/dedecms.css"', url) == "Pass" or auxiliary.searchLine('">DedeCMS</a>', url) == "Pass":
        print("您扫描的网站" + url + "可能是织梦(dede)cms")
        files.dedever(url)

    else:
        print("站点可能不是Dedecms哦~")
    pass


def allcms(url):
    discuz(url)
    Z_Blog(url)
    WordPress(url)
    dedecms(url)
    pass
