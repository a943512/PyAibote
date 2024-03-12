"""
	Mysql数据库操作
	Mysql database operation
"""
import pymysql
import os,sys,time
from .WriteReadFileFunc import  WriteReadFile
import traceback

class DataBaseHandle(WriteReadFile):
	def init_mysql(self):
		self.Path = f"{os.getcwd()}/ConfigFile.json"
		if not os.path.exists(self.Path):
			with open(self.Path,"w",encoding='UTF-8') as w:
				w.write('')

		self.USERNAME = WriteReadFile.ReadJsonFile(self,self.Path,"LinkDatabaseInfo","UserName")
		self.PASSWORD = WriteReadFile.ReadJsonFile(self,self.Path,"LinkDatabaseInfo","PassWord")
		self.DB = WriteReadFile.ReadJsonFile(self,self.Path,"LinkDatabaseInfo","DBName")
		self.host= WriteReadFile.ReadJsonFile(self,self.Path,"LinkDatabaseInfo","Host")
		self.port = WriteReadFile.ReadJsonFile(self,self.Path,"LinkDatabaseInfo","Port")
		
		# 打开数据库连接
		try:
			self.db = pymysql.connect(host=self.host,user=self.USERNAME,password=self.PASSWORD,database=self.DB,port=self.port,cursorclass=pymysql.cursors.DictCursor)
			return True
		except Exception as e:
			print("""请在ConfigFile.json 中配置你的数据库信息示例：
			 		{
						"LinkDatabaseInfo":{
							"UserName":"root",
							"PassWord":"12345678",
							"DBName":"pyaibote",
							"Host":"192.168.31.1",
							"Port":3306
						}
					}
				""")
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return False

	def Checkconnect(self):
		try:
			self.db.ping()
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")


	def insert_mysql(self,Sql):
		"""
			新增一条MySql数据库数据
			Add a MySql database data

			Sql: sql语句
			return: 成功返回True, 失败返回False

			Sql: sql statement
			return: Returns True on success and False on failure
		"""
		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			result = cursor.execute(sql)
			self.db.commit()
			if result ==1:
				return True
			else:
				return False
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return False


	def insertmany_mysql(self,Sql,Data):
		"""
			新增多条MySql数据库数据
			Add multiple MySql database data

			Sql: sql语句
			Data: 数据列表
			return: 成功返回True, 失败返回False

			Sql: sql statement
			Data: data list
			return: Returns True on success and False on failure
		"""
		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.executemany(Sql,Data)
			self.db.commit()
			return True
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return False
			
	def delete_mysql(self,Sql):
		"""
			删除MySql数据库数据
			Delete multiple MySql database data

			Sql: sql语句
			return: 成功返回True, 失败返回False

			Sql: sql statement
			return: True on success and False on failure
		"""

		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.execute(Sql)
			self.db.commit()
			return True
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return False

	def update_mysql(self,Sql):
		"""
			更新MySql数据库数据
			Update multiple MySql database data

			Sql: sql语句
			return: 成功返回True, 失败返回False

			Sql: sql statement
			return: True on success and False on failure
		"""

		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.execute(Sql)
			self.db.commit()
			return True
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return False

	def select_mysql(self,Sql):
		"""
			查询MySql数据库数据
			Query MySql database data

			Sql: sql语句
			return: 成功返回字典数据，失败返回Error

			Sql: sql statement
			return: dictionary data is returned successfully, and Error is returned if it fails
		"""

		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.execute(Sql)
			data=cursor.fetchall()
			return data

		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return False

			
	def close_mysql(self):
		try:
			if self.db:
				self.db.close()
			return True
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return False

