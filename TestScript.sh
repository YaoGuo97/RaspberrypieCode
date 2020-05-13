#!/bin/sh
while true
do
ps -ef | grep "/lzy/script/CarServer_Serial_start.py" | grep -v "grep"
	if [ "$?" -eq 1 ];then
		cd /lzy/shell_python_script 
		./CarServer_Serial_start.py
		echo "CarServer_Serial_start.py 服务正在重启!"
	else
		echo "CarServer_Serial_start.py 服务正在运行!"
	fi
	sleep 3
done