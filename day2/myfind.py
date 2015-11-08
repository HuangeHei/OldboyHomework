#-*- coding:utf-8 -*-
import sys

if __name__ == '__main__':
    print(u'欢迎来到德莱联盟')
    fp = open('data.db','r')
    i = 0
    while True:
        keyword = input(u'请输入要查找的关键字:')
        if keyword == 'quit':
            print("再见!!!")
            sys.exit()
        for line in fp.readlines():
            if line.find(keyword) != -1:
                print(line.strip())
                i+=1
        print(u'一共出现了:',i)
        i = 0
        fp.seek(0)
