#-*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall
import sys
import time
#import xlwt
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

inp = open('Mx_wei out2.txt','rb')
r = inp.readlines()
inp.close()
out = open('out222.txt','a')
sb = open('sb.txt','a+')


def request_web():
    for act in range(len(r)):
        page = urllib2.urlopen('https://baike.baidu.com/item/%s'%(r[act]))
        contents = page.read()
        soup = BeautifulSoup(contents, "html.parser")
        x = soup.find_all('dd', class_="basicInfo-item value")
        a = []
        b = []
#        get_info(a,b,soup)
#        out_put(a,b)
        time.sleep(1)
        if len(x) == 0:
            print >> out, "抱歉%s没找到"%(r[act])
            print >> sb,r[act]
          #  a.append("\n")
            continue
        print "--------------------手动分割----------------------------------",


def get_info(a,b,soup):
    for tag1 in soup.find_all('dd', class_="basicInfo-item value"):
        a.append(tag1.text)
    for tag in soup.find_all('dt', class_="basicInfo-item name"):
        b.append(tag.text)
    return


def out_put(a,b):
    count = 0
    for i in b:
        if i == "代表作品":
            pass
            print a[0] ,i,a[count],
            print >> out,a[0],i,a[count],
            print >> out, "----------------手动分隔符-------------------"
        count += 1



# page = urllib2.urlopen('https://baike.baidu.com/item/迪丽热巴' )
# contents = page.read()
# soup = BeautifulSoup(contents, "html.parser")
# a = []
# b = []
# for tag1 in soup.find_all('dd', class_="basicInfo-item value"):
#     a.append(tag1.text)
# for tag in soup.find_all('dt', class_="basicInfo-item name"):
#     b.append(tag.text)
# count = 0
# for i in b:
#     if i == "代表作品":
#         print i,a[count]
#     count += 1



if __name__ == '__main__':
    request_web()
