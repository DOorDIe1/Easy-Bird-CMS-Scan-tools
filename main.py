import os
import re
from urllib import request


def searchLine(keyLine):
    # searchLine代码来自：https://www.cnblogs.com/Amy20182018/articles/8962013.html
    f = open("web.txt", encoding='UTF-8')
    line = f.read()
    if keyLine in line:
        f.close()
        return "Pass"
    else:
        f.close()
        return "Failed"


def discuz(url):
    # 检测Discuz! X3.4
    if searchLine('Discuz! X3.4') == "Pass":
        {
            print("您扫描的网站" + url + "是Discuz！X3.4")
        }
    elif searchLine('Discuz! X3.3') == "Pass":
        {
            print("您扫描的网站" + url + "是Discuz！X3.3")

        }
    elif searchLine('Discuz! X3.2') == "Pass":
        {
            print("您扫描的网站" + url + "是Discuz！X3.2")
        }
    else:
        {
            print("站点可能不是Discuz哦~")
        }


def Z_Blog(url):
    # 检测Z-BlogPHP
    if searchLine('Z-BlogPHP') == "Pass":
        {
            print("您扫描的网站" + url + "是Z-BlogPHP")
        }
    elif searchLine('Z-BlogASP') == "Pass":
        {
            print("您扫描的网站" + url + "是Z-BlogASP")
        }
    elif searchLine('Z-Blog') == "Pass":
        {
            print("您扫描的网站" + url + "是Z-Blog")
        }
    else:
        {
            print("站点可能不是Z-Blog哦~")
        }


def WordPress(url):
    # 检测Z-BlogPHP
    if searchLine('WordPress 5.3.6') == "Pass":
        {
            print("您扫描的网站" + url + "是WordPress 5.3.6")
        }
    else:
        {
            print("站点可能不是WordPress哦~")
        }


def scan1():
    # 开始1号扫描
    print("欢迎使用Easy Bird CMS扫描器工具，现在在使用的是1号扫描。")
    url = input("Easy Bird > 输入您要扫描的地址 > ")
    page = request.urlopen(url)
    content = page.read()
    fp = open("web.txt", "w+b")  # 打开一个文本文件
    fp.write(content)  # 写入数据
    fp.close()  # 关闭文件
    discuz(url)  # discuz版本检测
    return 0


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
    print("""
    来自：天恩(Tianen)实验室开源
    QQ:1044631097
    QQ群：374327762
    项目协助：末心网络安全团队
    官方论坛：https://bbs.moxinwangluo.cn/
    项目Git地址：
    """)
    url = input("Easy Bird > 输入您要扫描的地址 > ")
    return 0


print("欢迎使用简鸟CMS识别工具，目前版本是0.11Beta。")
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
    2.关于
    Hint:目前只推出了两种选项，①是单纯识别CMS。
    """)
options1 = input("Easy Bird > ")
if options1 == "1":
    {
        scan1()
    }
elif options1 == "2":
    {
        scan2()
    }
