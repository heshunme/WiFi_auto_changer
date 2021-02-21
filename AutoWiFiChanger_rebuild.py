from time import sleep
from pywifi import PyWiFi
from subprocess import Popen, check_output, PIPE
from os import system
from json import load
from re import search


def get_wifi_profile():
    result = check_output(['netsh', 'wlan', 'show', 'profile'])
    result = result.decode('gbk')
    lst = result.split('\r\n')
    lst = lst[10:]
    li = []
    for index in range(len(lst)):
        t = search("(?<= : ).*", lst[index])
        if t is not None:
            li.append(t[0])
    return li


def scan_wifi():
    try:
        wifi_infos = []
        ava = []
        iface.scan()
        sleep(2)
        res = iface.scan_results()
    except:
        return
    ssid_temp = []  # 去重用
    for i in res:
        if i.ssid not in ssid_temp:
            ssid_temp.append(i.ssid)
        else:
            continue
        if i.ssid in ssids:
            ava.append(i.ssid)
            wifi_infos.append((i.ssid, i.bssid, i.signal))
    return ava, wifi_infos


def sort(a: list):  # 简单的选择排序
    for i in range(len(a)):
        k = i
        for j in range(i + 1, len(a)):
            if a[k][2] < a[j][2]:
                k = j
        if k != i:
            t = a[i]
            a[i] = a[k]
            a[k] = t
    return a


def get_current_wifi():
    cmd = 'netsh wlan show interfaces'
    p = Popen(cmd,
              stdin=PIPE,
              stdout=PIPE,
              stderr=PIPE,
              shell=True
              )
    ret = str(p.stdout.read())
    for i in available_wifi:
        if ret.find(i) > 0:
            return i
    return ""



def change_wifi(ssid):
    try:
        cmd = 'netsh wlan connect name="%s"' % ssid
        system(cmd)
    except:
        pass


path = "" # 改成运行目录
f = open(path + "options.ini", "r")
opt = load(f)
f.close()
while True:
    print(get_wifi_profile())
    try:
        iface = PyWiFi().interfaces()[0]
    except:
        sleep(opt["disconnect_wait_time"])
        continue
    ssids = get_wifi_profile()  # 保存过的wifi
    available_wifi, wifi_infos = scan_wifi()
    if len(available_wifi) > 0:
        print(wifi_infos)
        wifi_infos = sort(wifi_infos)
        best_wifi = wifi_infos[0][0]
        current_wifi = get_current_wifi()
        if current_wifi != best_wifi:
            change_wifi(best_wifi)
    sleep(opt["sleep_time"])
