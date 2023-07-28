# -*- coding: utf-8 -*-
from dataclasses import dataclass
import yaml
import psycopg2
from config.conf import config


@dataclass()
class ConfBase:
    host: str
    port: int
    dbname: str
    user: str
    password: str


conf = ConfBase(**config)


# @classmethod
class PostgresTool():

    # @staticmethod
    def __init__(self):
        self.host = conf.host
        self.port = conf.port
        self.dbname = conf.dbname
        self.user = conf.user
        self.password = conf.password
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )
        self.cur = self.conn.cursor()

    # @staticmethod # 不用对象属性，也不用对象方法
    # @classmethod
    def select(self, table, columns=None, condition=None):
        """查询数据"""
        if columns is None:
            columns = '*'
        sql = f"SELECT {columns} FROM {table}"
        if condition:
            sql += f' WHERE {condition}'
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert(self, table, data):
        """插入数据"""
        keys = ','.join(data.keys())
        values = ','.join(['%s'] * len(data))
        sql = f'INSERT INTO {table} ({keys}) VALUES ({values})'
        self.cur.execute(sql, list(data.values()))
        self.conn.commit()

    def update(self, table, data, condition):
        """更新数据"""
        sets = ','.join([f'{k}=%s' for k in data.keys()])
        sql = f'UPDATE {table} SET {sets} WHERE {condition}'
        self.cur.execute(sql, list(data.values()))
        self.conn.commit()

    def delete(self, table, condition):
        """删除数据"""
        sql = f'DELETE FROM {table} WHERE {condition}'
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        """关闭数据库连接"""
        self.cur.close()
        self.conn.close()
    # pass


pos = PostgresTool()
if __name__ == '__main__':
    pass
    # print(conf.host)
    # p = PostgresTool()
    # print(p.host)
    # p.select()
