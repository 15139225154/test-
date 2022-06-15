'''
ip = '192.168.137.1'
user = 'root'
pwd = '123456'
port = 3306
dbm = 'huogedb'
'''
import pymysql

from UI_active.common.common_date import Yaml


class Mysql_py():
    def __init__(self,sql_type,sql):
        ip = Yaml()['ip']
        user = Yaml()['user']
        pwd = Yaml()['pwd']
        port = Yaml()['port']
        dbm = Yaml()['dbm']
        #连接数据库
        self.db = pymysql.connect(host=ip,user=user,passwd=pwd, port = port,db=dbm,charset='utf8')
        #使用cursor（）方法获取操作游标
        self.cursor = self.db.cursor()
        self.sql_sentence(sql_type,sql)
        self.close_sql()


    def sql_sentence(self,sql_type,sql):
        if sql_type == 'select':
            self.select_sql(sql)
        elif sql_type == 'update':
            self.update_mysql(sql)
        elif sql_type == 'insert':
            self.insert_mysql(sql)
        elif sql_type == 'delete':
            self.delete_mysql(sql)




    #sql语句查询
    def select_sql(self,sql):
        # sql = "SELECT * FROM cjb"
        try:
            #执行sql语句
            self.cursor.execute(sql)
            #获取所有记录列表
            result = self.cursor.fetchall()
            print(result)
            for col in result:
                id = col[0]
                name = col[1]
                class1 = col[2]
                score = col[3]
                print(id,name,class1,score)
        except:
            print('error1')

        return result

    #sql修改
    def update_mysql(self,sql):
        #sql = "UPDATE cjb  SET score='81' WHERE id='01'"
        try:
            #执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            self.db.rollback()

    #sql插入数据
    def insert_mysql(self,sql):
        #sql = "INSERT INTO cjb (id,name,class,score) VALUES ('02','李四','二年级','99');"
        try:
            #执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            self.db.rollback()

    #sql删除数据
    def delete_mysql(self,sql):
        #sql = "DELETE FROM cjb WHERE  id='02'"
        try:
            #执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            self.db.rollback()

    #关闭数据库
    def close_sql(self):
        self.db.close()

if __name__ == '__main__':
    Mysql_py('update',"UPDATE cjb  SET score='99' WHERE id='01'")
    Mysql_py('select',"SELECT * FROM cjb")






