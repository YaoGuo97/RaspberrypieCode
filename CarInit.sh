#!/bin/sh

# 1.进入脚本文件夹
cd /lzy/script
if [ $? -eq 0 ];then
	echo "进入目录 /lzy/script 成功！"
else
	echo "进入目录 /lzy/script 失败！"
fi

# 2.创建热点
./CreateAP.sh &
if [ $? -eq 0 ];then
	echo "执行 CreateAP.sh 成功！"
else
	echo "进入目录 CreateAP.sh 失败！"
fi
	
# 4.开启socket通信 服务端 
# 并且监听程序是否在执行，如果没执行，则自动执行
./TestScript.sh &
if [ $? -eq 0 ];then
	echo "执行 TestScript.sh 成功！"
else
	echo "进入目录 TestScript.sh 失败！"
fi

# 3.开启摄像头程序并后台运行 
./lzy_RaspberryPie_Code.sh &
if [ $? -eq 0 ];then
	echo "执行 lzy_RaspberryPie_Code.sh 成功！"
else
	echo "进入目录 lzy_RaspberryPie_Code.sh 失败！"
fi
