# 2022 MCM获取代码 v1

## 准备

1.pip安装所需包

2.下载tesseract软件，并且在ocr.py中更改第十行路径为你的安装路径（tesseract.exe)

3.准备一个excel表格，确保有名为Control Number的一列，命名为1.xlsx

4.为了速度更快建议科学，全局代理后，由于urlib3的一个bug会导致出错，需要更改request的源码，具体修改见https://github.com/python/cpython/pull/26307/files?diff=unified&w=0#

## 开始运行

1.cmd中cd 到当前目录下，执行python mcm.py，下载证书至./certificates

2.执行python ocr.py，输出结果至award.csv

# v2

更新了学校、队员的获取；