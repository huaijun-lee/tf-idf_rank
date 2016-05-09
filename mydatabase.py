# -*- coding: utf-8 -*-
# Windows python3.5
# Spyde2
__author__ = 'huaijun'
import os
from os import path
from ZODB import FileStorage, DB
import transaction
from pickle import load
class MyZODB(object):
    def __init__(self, path):
        self.storage = FileStorage.FileStorage(path)
        self.db = DB(self.storage,create=True, large_record_size=999)
        self.connection = self.db.open()
        self.dbroot = self.connection.root()       
    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()
class database():
	"""docstring for database"""
	def __init__(self):
		super(database, self).__init__()
		self.rootdirs = os.getcwd()
	def todatabese(self):
         databaseurl = path.join(self.rootdirs,'database')
         if not path.isdir(databaseurl):
             os.mkdir(databaseurl)
         db = MyZODB(path.join(databaseurl,'mydatabase.fs'))
         dbroot = db.dbroot
         dictdirs = os.listdir(databaseurl)
         dictdirs = [ele for ele in dictdirs if ele.startswith('C0') and ele.endswith('.pickle')]
         for D in dictdirs:
             folderdict = load(open(path.join(databaseurl,D),'rb'))
             name = D.split('.')[0]
             dbroot[str(name)] =folderdict
         transaction.commit()
         db.close()
mydb = database()
mydb.todatabese()

