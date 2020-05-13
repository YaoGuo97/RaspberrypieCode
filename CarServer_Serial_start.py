#! /usr/bin/python
#coding=utf-8

import socket
import serial
import time
import sys
import os

# Explain
# 用途：2020届物联网工程本科毕业设计
# 题目：基于Arduino与树莓派的无线视频小车
# 作者：刘祖耀
# Failname : CarServer_Serial_start.py
# chmod 777 CarServer_Serial_start.py  需要先给执行权限
# 本程序实现功能有如下两部分: filename =
# 1.socket | 安卓与树莓派之间的通信
# 2.Serial port | 树莓派与Arduino之间的通信

HOST_IP = "0.0.0.0"  # 我的树莓派作为AP热点的IP地址 允许任意IP
HOST_PORT = 8081         # 服务端端口号

print("Starting socket: TCP...")

# 创建socket
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP server Listen @ %s:%d!" % (HOST_IP, HOST_PORT))
host_addr = (HOST_IP, HOST_PORT)

# 绑定我的树莓派的IP地址和端口号
socket_tcp.bind(host_addr)

# Listen函数的参数是监听客户端的个数，这里只监听一个，即只允许与一个客户端创建连接
socket_tcp.listen(5)

# 使用树莓派的GPIO口连接串行口
ser = serial.Serial('/dev/ttyAMA0', 9600)
if ser.isOpen():
    print("串口开启成功!")
ser.write(b'Raspberry pi is ready\n')

while True:

    print("waiting for connection...")
    
    # 接受客户端请求
    socket_con, (client_ip, client_port) = socket_tcp.accept()
    print("Connection accepted from %s." %client_ip)

    # 发送数据 连接成功
    str = "Welcome to RPi TCP server!"
    socket_con.send(str.encode())

    while True:
        try:
            # 接受数据
            data = socket_con.recv(1024)

            # 如果数据不为空，则打印数据，并将数据转发给客户端
            if data:
            
                # 打印字符 解码字符
                data = data.decode("utf8", "ignore");
                print(data)
                
                # 将数据转发给Arduino芯片
                ser.write(data + '\n')
                
                # 数据回显 APP显示
                temp = 'from server: ' + data;
                socket_con.send(temp.encode())
                
        except ConnectionResetError as e:
            print('client disconnected...')
            break
        
        # 判断用户是否要关闭树莓派
        if data == "pshut":
            os.system('init 0')

        # 判断客户端是否断开连接
        if data == b'' or data == "disconnect":
            break

socket_tcp.close()
