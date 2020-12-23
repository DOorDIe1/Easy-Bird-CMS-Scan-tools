import auxiliary
import files


def discuzrobots(url, uurl):
    if auxiliary.searchLine('Discuz! X3', url) == "Pass":
        print("从robots.txt检测中得到", url, "可能是Discuz X3站点！")
    if auxiliary.searchLine('/uc_server/', url) == "Pass":
        print("从robots.txt检测中得到", url, "可能是Discuz X3站点！（存在uc_server）")
    pass


def dederobots(url, uurl):
    if auxiliary.searchLine('/plus/feedback_js.php', url) == "Pass":
        print("从robots.txt检测中得到", url, "可能是dedecms站点！")
        files.dedever(uurl)
    if auxiliary.searchLine('/plus/shops_buyaction.php', url) == "Pass":
        print("从robots.txt检测中得到", url, "可能是dedecms站点！")
        files.dedever(uurl)
    pass


def allrobots(url, uurl):
    discuzrobots(url, uurl)
    dederobots(url, uurl)
    pass
