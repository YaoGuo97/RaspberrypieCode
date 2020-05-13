#!/usr/bin/python
# coding=utf-8

import serial
import time

# 使用树莓派的GPIO口连接串行口
ser = serial.Serial('/dev/ttyAMA0', 115200)
if ser.isOpen():
    print("串口开启成功!")
ser.write(b'Raspberry pi is ready\n')
print("wait for...")
try:
    while True:
        # 获得缓冲区字符
        count = ser.inWaiting()
        if count != 0:
            # 读取内容并显示
            accept_data = ser.read(count)
            print(accept_data)
            # 回显
            ser.write(accept_data)
            # 清空显示区
            ser.flushInput()
            # 延时一下
            time.sleep(0.1)
except KeyboardInterrupt:
    ser.close()
