# Author:zhouxy
#-*-coding:gbk-*-

str='���'
print(str.encode('utf-8').decode('utf-8').encode('gb2312'))
