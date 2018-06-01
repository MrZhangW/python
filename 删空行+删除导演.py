#coding=utf-8
import urllib2
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall
import sys
import io
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def clearBlankLine():
    file1 = io.open('Mx_out1.txt', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = io.open('out_Mx.txt', 'w+', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            # if len(line.strip().split("没有")) == 1:
            #     print >>
            if len(line.strip().split("导演")) == 1:
                if len(line.strip().split("主演")) == 1:
                    file2.write(line)
    # finally:
    #     file1.close()
    #     file2.close()

        for  i  in  file2.readlines():
            if "没有找到" in i:
                print >> file2,"---------------手动分隔符-------------"
    finally:
        file1.close()
        file2.close()

if __name__ == '__main__':
    clearBlankLine()
