"""
	Mysql数据库操作
	Mysql database operation
"""
import pymysql
import os,sys,time
from .WriteReadFileFunc import  WriteReadFile
import traceback

class DataBaseHandle(WriteReadFile):
	def database_init(self):
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
			

	def Checkconnect(self):
		try:
			self.db.ping()
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")


	def insertDB(self,sql):
		"""
			插入数据库操作
			Insert database operation
		"""
		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			result = cursor.execute(sql)
			self.db.commit()
			if result ==1:
				return 'Ok'
			else:
				return 'Error'
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return 'Error'

	def insertDBPathLoss(self,sql):
		"""
			插入数据库操作
			Insert database operation
		"""

		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.execute(sql)
			InsertId = int(cursor.lastrowid)
			result = self.db.commit()
			return InsertId
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return 'Error'
			
	def insertmanyDB(self,sql,data):
		"""
			插入多笔数据到数据库
			Insert multiple data into the database
		"""
		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.executemany(sql,data)
			self.db.commit()
			return 'Ok'
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return 'Error'
			
	def deleteDB(self,sql):
		"""
			删除操作
			Delete database operation
		"""

		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.execute(sql)
			self.db.commit()
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return 'Error'

	def updateDB(self,sql):
		"""
			更新操作操作
		"""

		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.execute(sql)
			self.db.commit()
			return 'Ok'
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return 'Error'

	def selectDB(self,sql):
		"""
			查询动作
		"""

		try:
			self.Checkconnect()
			cursor = self.db.cursor()
			cursor.execute(sql)
			data=cursor.fetchall()
			return data

		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")
			return 'Error'

			
	def close(self):
		try:
			if self.db:
				self.db.close()
		except Exception as e:
			WriteReadFile.Custom_Write_logger(self,"",f"{os.getcwd()}/AiBotRunLOG/{time.strftime(r'%Y-%m-%d',time.localtime(time.time()))}/","SysModeError.log",f"{traceback.format_exc()}")

