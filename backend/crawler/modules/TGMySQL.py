# coding=utf-8

import pymysql
import time


class TGMySQL:
    def __init__(self, file_name, user="william", password="william", db_name="TESTDB"):
        flag = True
        while flag:
            try:
                self.db = pymysql.connect("db", "william", "william", "TESTDB")
                flag = False
            except:
                print("等待 SQL Server 啟動")
                time.sleep(1)

        self.cursor = self.db.cursor()
        self.tableName = file_name[:-3]
        print("Connected db")

    def connect_SQL(self):
        sql = """CREATE TABLE %s(
            TITLE  CHAR(255) NOT NULL,
            OFFICE  CHAR(40),
            LINK  varchar(500),
            DATA CHAR(40))
            """ % self.tableName
        try:
            self.cursor.execute(sql)
            
        except:
            self.db.rollback()
            print("找到資料表：%s" % self.tableName)

    def check_SQL(self, title):
        print(self.tableName)
        sql = "SELECT count( * ) FROM `%s` WHERE `TITLE` = '%s'" % (self.tableName, title)
        print(sql)
        self.cursor.execute(sql.lstrip())
        result = self.cursor.fetchone()[0]
        print(result)
        if result == 0:
            return True
        else:
            return False

    def insert_SQL(self, TITLE, OFFICE, LINK, DATA):
        sql = "INSERT INTO %s(TITLE, OFFICE, LINK, DATA) VALUES ('%s', '%s', '%s', '%s')" % (
            self.tableName, TITLE, OFFICE, LINK, DATA)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def close_SQL(self):
        self.db.close()
