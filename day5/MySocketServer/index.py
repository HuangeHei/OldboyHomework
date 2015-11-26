#coding:utf-8
import socketserver
from conf import HostName
from utility.MySocketServer import MySocketServer 


if __name__  == '__main__':
    sk = socketserver.ThreadingTCPServer(HostName,MySocketServer)
    sk.serve_forever()