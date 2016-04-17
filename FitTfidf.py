# -*- coding: utf-8 -*-
# Windows python3.5
# Spyde2
__author__ = 'huaijun'
import os
from os import path
from pickle import load,dump

from fit_idf import globalidf
from segword import cut_for_search
class TFIDF(object):
	"""docstring for TFIDF"""
	def __init__(self):
		super(TFIDF, self).__init__()
		self.rootdirs = os.getcwd()
	def count(self,words):
		words_list = words.split(' ')
		tf_dict = {}
		for word in words_list:
			if word not in tf_dict.keys():
				tf_dict[word] = 1
			else:
				tf_dict[word] += 1
		return tf_dict
	def totfidf(self,bigidf,segdict):
		folderdict ={}
		for filename,segwords in segdict.items():
                  tfidf_dict = self.count(segwords)                     
                  for term in tfidf_dict.keys():
                      try:
                        tfidf_dict[term] = tfidf_dict[term]*bigidf[term]
                        folderdict[str(filename)] = tfidf_dict
                      except (KeyError, NameError, FileNotFoundError):
                        pass
		return folderdict
	def main(self):
         segfolder = path.join(self.rootdirs,'seg')
         databaseurl = path.join(self.rootdirs,'database')
         if not path.isdir(databaseurl):
             os.mkdir(databaseurl)
         filerdir = os.listdir(segfolder)	
         filerdir = [ele for ele in filerdir if ele.startswith('segdict') and ele.endswith('pickle')]
         try:
             bigidf = load(open(path.join(self.rootdirs,'globalidf.pickle'),'rb'))
             print('成功加载全局idf')
         except (IOError, NameError, FileNotFoundError):
             idf = globalidf()
             idf.bigidf()
             bigidf = load(open(path.join(self.rootdirs,'globalidf.pickle'),'rb'))
         if not len(filerdir) == 9:
             cutwords = cut_for_search()
             cutwords.main_files()
         else:
             print('成功加载分词数据')
         for seg in filerdir:			
            segdict = load(open(path.join(segfolder,seg),'rb'))
            folderdict = self.totfidf(bigidf,segdict)
            name = str(seg).split('_')[1]
            dump(folderdict,open(path.join(databaseurl,name + '.pickle'),'wb'))
tfidf = TFIDF()
tfidf.main()			