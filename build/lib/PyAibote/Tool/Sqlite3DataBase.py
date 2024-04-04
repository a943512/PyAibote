"""
	操作sqlite3数据库
	Operating sqlite3 database
"""
import os,sys,time
import sqlite3
import traceback 
from .WriteReadFileFunc import  WriteReadFile

class Sqlite3DataBaseHandle(WriteReadFile):
	def init_sqlite3(self) -> bool:
		self.Path = f"{os.getcwd()}/ConfigFile.json"
		if not os.path.exists(self.Path):
			with open(self.Path,"w",encoding='UTF-8') as w:
				w.write('')

		Sqlite3_DB_Path = WriteReadFile.ReadJsonFile(self,self.Path,"Sqlite3_DB")

		# 打开数据库连接
		try:
			self.conn = sqlite3.connect(Sqlite3_DB_Path, check_same_thread=False)
			self.cursor = self.conn.cursor()
			return True
		except Exception as e:
			print("""请在ConfigFile.json 中配置你的数据库信息示例：
			 		{
						"Sqlite3_DB":"D:\\Project\\Coding\\PyAibote\\DB\\Pyaibote.db"
					}
				""")
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",False,f"{traceback.format_exc()}")
			return False

	def dict_factory(self, cursor, row) -> list:
		"""
			元祖变成字典
			Yuanzu became a dictionary

			cursor: sql对象
			row: 查询出来的数据集
			return: 列表

			cursor: sql object
			row: the queried data set
			return: list
		"""
		DictList = []
		if row:
			col = cursor.description
			for RowData in row:
				DataDict = {}
				for idx  in range(len(RowData)):
					DataDict[col[idx][0]] = RowData[idx]
				DictList.append(DataDict)
		return DictList


	def insert_delete_update_sqlite3(self,sql) -> bool:
		"""
			新增, 删除, 更新 sqlite3数据库数据
			Insert data, delete data, update data

			sq: 插入数据, 删除数据, 更新数据的sql语句
			return: 成功返回True, 失败返回False

			sql:sql statements for inserting data, deleting data and updating data
			return:  True on success and False on failure
		"""
		try:
			self.cursor.execute(sql)
			self.conn.commit()
			return True
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",False,f"{traceback.format_exc()}")
			return False

	def select_sqlite3(self,sql)  -> list: 
		"""
			查询sqlite3数据库
			Query sqlite3 database

			sql: 查询数据库的sql语句
			return: 查询的列表数据数据或者False

			sql: sql statement for querying the database
			return: Query list data data or False
		"""
		try:
			cur = self.cursor.execute(sql)
			data = cur.fetchall()
			data = self.dict_factory(cur, data)
			return data
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",False,f"{traceback.format_exc()}")
			return False

	def close_sqlite3(self)  -> bool:
		"""
			关闭sqlite3数据库
			Close the sqlite3 database

			return: 布尔值
			return: boolean value
		"""
		try:
			self.conn.close()
			return True
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",False,f"{traceback.format_exc()}")
			return False



