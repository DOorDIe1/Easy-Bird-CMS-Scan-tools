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


def otherscan(url):
    print("是否要对该站点进行自动响应点扫描？[Y/n]")  # 即将做的一套后台扫描的雏形
    vlan = input("Easy Bird > Auto Scan >  ")
    if vlan == 'Y' or vlan == "y" or vlan == "":  # 如果直接回车程序会默认为Y
        auto(url)


def auto(url):
    if auxiliary.http_status(url + "/dede/login.php") == 200:
        print("扫描到Dede后台登陆页面！", url + "/dede/login.php")
    if auxiliary.http_status(url + "/admin.php") == 200:
        print("扫描到后台登陆页面！", url + "/admin.php")
    if auxiliary.http_status(url + "/admin") == 200:
        print("扫描到后台登陆页面！", url + "/admin")
    if auxiliary.http_status(url + "/admin/login.php") == 200:
        print("扫描到后台登陆页面！", url + "/admin/login.php")


pass
