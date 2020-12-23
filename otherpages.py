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
