# -*- coding: utf-8 -*-
# Windows python3.5
# Spyde2
__author__ = 'huaijun'
import os
from os import path
from sklearn.feature_extraction.text import TfidfVectorizer
from pickle import dump, load

from segword import cut_for_search
class globalidf():
	"""docstring for globalidf
	计算全部文档（即该语料库）的IDF值，并以dict形式dump到本地"""
	def __init__(self):
		super(globalidf, self).__init__()
		self.rootdir = os.getcwd()
	def bigidf(self):
		rootfloder = path.join(self.rootdir,'seg')
		filerdir = os.listdir(rootfloder)	
		filerdir = [ele for ele in filerdir if ele.startswith('segdict') and ele.endswith('pickle')]
		if not len(filerdir) == 9:
			cutwords = cut_for_search()
			cutwords.main_files()
		else:
			print('成功加载分词数据')
		concentlist = []
		for D in filerdir:
			segdict = load(open(path.join(rootfloder,D),'rb'))
			for words in segdict.values():
				concentlist.append(words)
		vect = TfidfVectorizer()
		vect.fit(concentlist)
		idf_values = vect.idf_
		idf_keys = vect.get_feature_names()
		idf_dict = dict(zip(idf_keys,idf_values))
		dump(idf_dict,open(path.join(self.rootdir,'globalidf.pickle'),'wb'))
