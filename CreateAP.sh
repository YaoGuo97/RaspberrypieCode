#!/bin/sh

# 关闭wlan0并创建热点
#wlan0 无线网卡  #eth0 有线网卡
ifdown wlan0
# 参数解释 热点名称 wifi密码 & 后台运行		
create_ap wlan0 eth0 YaoGuo_WiFi 123456789 &


