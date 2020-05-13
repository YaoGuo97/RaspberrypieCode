#!/bin/sh

# Explain 
# 用途：2020届物联网工程本科毕业设计
# 题目：基于Arduino与树莓派的无线视频小车
# 作者：刘祖耀 
# Failname : lzy_RaspberryPie_Code.sh 
# chmod 777 lzy_RaspberryPie_Code.sh  需要先给执行权限 
# 本程序实现功能有如下两部分: 
# 1.cd | 进入到指定的目录
# 2.if | 检测程序能否运行成功

#该文件写好后 将./lzy/software/mjpg-streamer-code-182/mjpg-streamer 追加到rc.local文件中，exit0之前
cd /lzy/software/mjpg-streamer-master/mjpg-streamer-experimental
if [ $? -eq 0 ];then
	echo "进入目录 /lzy/software/mjpg-streamer-master/mjpg-streamer-experimental 成功！"
	./mjpg_streamer -i "./input_raspicam.so" -o "./output_http.so -w ./www"
	if [ $? -eq 0 ];then
		echo "执行 start.sh 成功,摄像头开启成功！"
	else
		echo "执行 start.sh 失败,摄像头开启失败！"
	fi
else 
	echo "进入目录 /lzy/software/mjpg-streamer-master/mjpg-streamer-experimental 失败！"
fi
