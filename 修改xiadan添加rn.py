import os

with open('C:\\Users\\Ths\\Desktop\\XIADAN.ini', 'rb') as fr:  # 用字节打开可避免编码问题
    with open('C:\\Users\\Ths\\Desktop\\XIADAN加rn版.ini', 'wb') as fw:
        for l in fr:
            fw.write(l.replace(b'\r\n', b'\\r\\n\r\n'))
            # 上面适用于win格式文本，*nix格式不需要'\r', mac格式忘了，自己查一下
# 下面是如果需要覆盖原文件fn.txt使用，否则跳过

#os.rename('C:\\Users\\Ths\\Desktop\\XIADAN.ini', 'C:\\Users\\Ths\\Desktop\\fn.bak')  # 代码测试成功这句可改用os.remove
#os.rename('C:\\Users\\Ths\\Desktop\\XIADAN1.ini', 'C:\\Users\\Ths\\Desktop\\fn.txt')

path = r'C:\\Users\\Ths\\Desktop\\XIADAN加rn版.ini'#文本存放的路径
with open(path) as file:
    lines = file.readlines()#读取每一行

a = ''#空字符（中间不加空格）
for line in lines:
    a += line.strip()#strip()是去掉每行末尾的换行符\n 1
c = a.split()#将a分割成每个字符串 2
#b = ''.join(c)#将c的每个字符不以任何符号直接连接 3
print(a)
doc = open('C:\\Users\\Ths\\Desktop\\XIADAN加rn版.ini','w')
print(a,file=doc)
doc.close()
