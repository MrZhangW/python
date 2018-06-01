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

inp = open('in.txt','rb')
out = open('Mx_out1.txt','a+')
out2 = open('Mx_out2.txt','a+')

r = inp.readlines()

proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
#a = []
for act in range(len(r)):
    page = urllib2.urlopen('https://baike.baidu.com/item/%s'%(r[act]))
    contents = page.read()
    soup = BeautifulSoup(contents, "html.parser")
    x1 = soup.find_all('div', class_="info")
    if len(x1) == 0 :
        print >> out2, r[act]
        print >> out,r[act],"饰演无"
        continue
    for tag in soup.find_all('div',class_="info"):
        pass
       #  print r[act],x[1].text,x[2].text
        #a.append(tag)
    print r[act],x1[0].text
    print >> out, "《%s》"%(x1[0]).text

out2.close()

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
