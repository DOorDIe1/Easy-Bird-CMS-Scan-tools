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
import otherpages
import adminscan

# 调用辅助模块


'''
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
'''


def scan1():
    # 开始1号扫描
    print("""
              '||''''|                           '||'''|,                  ||` 
               ||   .                             ||   ||   ''             ||  
               ||'''|   '''|.  ('''' '||  ||`     ||;;;;    ||  '||''| .|''||  
               ||      .|''||   `'')  `|..||      ||   ||   ||   ||    ||  ||  
              .||....| `|..||. `...'      ||     .||...|'  .||. .||.   `|..||. 
                                       ,  |'                                   
                                        ''                                     """)
    print("欢迎使用Easy Bird CMS扫描器工具，现在在使用的是1号扫描。")
    print("请输入网址，格式为：http://xxx或https://xxx！！！")
    url = input("Easy Bird > CMS Scan > ")
    # 检查访问状态
    print("当前网站访问状态为：", auxiliary.http_status(url))
    if auxiliary.http_status(url) == 200:
        print("当前网站编码类型为：", auxiliary.http_type(url))
        page = request.urlopen(url)
        content = page.read()
        fp = open("date\\web.txt", "w+b")  # 打开一个文本文件
        fp.write(content)  # 写入数据
        fp.close()  # 关闭文件
        '''
        cms.discuz(url)  # discuz版本检测
        cms.Z_Blog(url)  # Z-blog检测
        cms.WordPress(url)  # WordPress检测
        cms.dedecms(url)  # dedecms检测
        '''
        cms.allcms(url)  # 2020年12月23日整合
        # 完成首页检测后进行robots文件检测
        urlrobots = url + "/robots.txt"  # 需要做Linux大小写兼容
        # 检测robots.txt是否存在
        # 完成首页检测后，删除文件
        os.remove("date\\web.txt")

        if auxiliary.http_status(urlrobots) == 200:
            print("auxiliary模块检测到此网站存在robots.txt，请问是否对其进行检测？[Y/n]")
            vlan = input("Easy Bird > Robots Scan >  ")
            if vlan == 'Y' or vlan == "y" or vlan == "":  # 如果直接回车程序会默认为Y
                page = request.urlopen(urlrobots)
                content = page.read()
                fp = open("date\\robots.txt", "w+b")  # 打开一个文本文件
                fp.write(content)  # 写入数据
                fp.close()  # 关闭文件
                robotsscan.allrobots(urlrobots, url)
            else:
                otherpages.otherscan(url)
        else:
            otherpages.otherscan(url)

        return 0


pass


def scan2():
    print("""
          '||''''|                           '||'''|,                  ||` 
           ||   .                             ||   ||   ''             ||  
           ||'''|   '''|.  ('''' '||  ||`     ||;;;;    ||  '||''| .|''||  
           ||      .|''||   `'')  `|..||      ||   ||   ||   ||    ||  ||  
          .||....| `|..||. `...'      ||     .||...|'  .||. .||.   `|..||. 
                                   ,  |'                                   
                                    ''                                     """)
    print("\n")
    print("请输入网址，格式为：http://xxx或https://xxx！！！")
    adurl = input("Easy Bird > Admin Scan > ")
    print("请输入扫描延时，单位为毫秒(默认20)")
    delays = input("Easy Bird > Admin Scan > ")
    if delays == "":
        delays = 0.020 # 1s = 1000ms
    delays = int(delays) / 1000

    print("请选择扫描类型：")
    print("""
        1.PHP
        2.ASP
        3.ASPX
        4.JSP
        5.DIR
        6.MDB
        7.SQL
    """)
    scanv = input("Easy Bird > Admin Scan > ")
    if scanv == '1':
        adminscan.adminscan_php(adurl, delays)
    elif scanv == '2':
        adminscan.adminscan_asp(adurl , delays)
    elif scanv == '3':
        adminscan.adminscan_aspx(adurl , delays)
    elif scanv == '4':
        adminscan.adminscan_jsp(adurl , delays)
    elif scanv == '5':
        adminscan.adminscan_dir(adurl , delays)
    elif scanv == '6':
        adminscan.adminscan_mdb(adurl , delays)
    elif scanv == '7':
        adminscan.adminscan_sql(adurl , delays)
    return 0
    pass


def scan3():
    print("""
              '||''''|                           '||'''|,                  ||` 
               ||   .                             ||   ||   ''             ||  
               ||'''|   '''|.  ('''' '||  ||`     ||;;;;    ||  '||''| .|''||  
               ||      .|''||   `'')  `|..||      ||   ||   ||   ||    ||  ||  
              .||....| `|..||. `...'      ||     .||...|'  .||. .||.   `|..||. 
                                       ,  |'                                   
                                        ''                                     """)
    print("\n")
    print("""
        来自：天恩(Tianen)实验室开源
        QQ:1044631097
        QQ群：374327762
        项目协助：末心网络安全团队
        官方论坛：https://bbs.moxinwangluo.cn/
        项目Git地址：https://github.com/Moxin1044/Easy-Bird-CMS-Scan-tools
        """)
    url = input("Easy Bird > About > ")
    return 0
    pass

print("欢迎使用简鸟CMS识别工具，目前版本是1.2alph。")
print("项目已经公测，欢迎各位dalao给出意见。")
print("\n")
print("\n")
'''
在此处添加更新检测代码
'''
print("""
      '||''''|                           '||'''|,                  ||` 
       ||   .                             ||   ||   ''             ||  
       ||'''|   '''|.  ('''' '||  ||`     ||;;;;    ||  '||''| .|''||  
       ||      .|''||   `'')  `|..||      ||   ||   ||   ||    ||  ||  
      .||....| `|..||. `...'      ||     .||...|'  .||. .||.   `|..||. 
                               ,  |'                                   
                                ''                                     """)
print("\n")
print("请选择您需要的选项来进行操作，在下方回复序号即可。")
print("""
    1.CMS识别
    2.后台扫描
    3.关于
    Hint:目前只推出了两种选项，①是单纯识别CMS。
    """)
options1 = input("Easy Bird > ")
if options1 == "1":
    scan1()
elif options1 == "2":
    scan2()
elif options1 == "3":
    scan3()