#coding:utf-8

import socketserver
from model.BaseMySql import MySql
import pickle

class MySocketServer(socketserver.BaseRequestHandler):
    
    def setup(self):
        pass

    def handle(self):
        
        conn = self.request
        conn.send('Welcome'.encode())
        flag = True
        while flag:
            
            data = conn.recv(100)
            UserInfo=pickle.loads(data.decode('utf-8'))
            if MySql.SelectUserPasswd(UserInfo[0],UserInfo[1]):
                conn.send('ok'.encode())
                flag = False
            else:
                conn.send('no'.encode())
        
        flag2 = True
        while flag2:
            data = conn.recv()
            if data.decode('utf-8') == 'exit':
                flag2 = False
            else:
                conn.send('HaHa')
                
    def finish(self):
        pass
    