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
