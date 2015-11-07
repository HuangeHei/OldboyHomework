#-*- coding:utf-8 -*-
import sys

if __name__ == '__main__':

    print('Welcome to Ubuntu 14.10')
    user = input('login:')
    fp = open('data.txt','r')
    
    for line in fp:
        user_info = line.split(':')
          
    fp.close()
    
    if user_info[0] == user:
        error = int(user_info[2])
        if error >= 2:
            print('用户被锁定')
            sys.exit(1)
            
        while True:
            passwd = input('passwd:')
            if passwd == user_info[1]:
                print('[huanghei@huanghei ~]$')
                sys.exit(0)
            else:
                print('Passwd error')
                error+=1
                fp = open('data.txt','w')
                fp.write(user_info[0]+':'+user_info[1]+':'+str(error))
            if error >= 3:
                print('用户被锁定')
                sys.exit(1)
                
            
            
        
        
    
