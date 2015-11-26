#coding:utf-8
import pymysql
from conf import SqlName
class MySql():
    def __init__(self):
        pass
    
    @staticmethod
    def SelectUserPasswd(self,user,passwd):
        conn  = pymysql.connect(**SqlName)
        cur = conn.cursor()
        ret = cur.execute('select * from %s where UserName = "%s" and UserPasswd="%s"',(SqlName['db'],user,passwd))
        
        if ret:
            cur.close()
            conn.close()
            return(1)
        else:
            cur.close()
            conn.close()
            return(0)
    
    
    