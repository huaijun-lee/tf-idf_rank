# -*- coding: utf-8 -*-
# Windows python3.5
# Spyde2
__author__ = 'huaijun'
import os
import collections
from os import path
from pickle import load
from time import clock
from numpy import array
from math import sqrt
import jieba.analyse

class dealquery(object):
	"""docstring for dealquery"""
	def __init__(self, sentence):
		super(dealquery, self).__init__()
		self.sentence = sentence
		self.rootdir = os.getcwd()
		self.words = self.cut_seg()
		self.n = len(self.words)
	def data(self):
		dataurl = path.join(self.rootdir,'database')
		datadir = os.listdir(dataurl)
		datadirurl = [path.join(dataurl,ele) for ele in datadir if ele.startswith('C0') and ele.endswith('.pickle')]	
		return datadirurl		
	def cut_seg(self):
		words = jieba.analyse.extract_tags(self.sentence, topK=10, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
		wordlist = []
		self.weight = []
		for word,weig in words:
			wordlist.append(word)
			self.weight.append(weig)
		return wordlist
	def count_sum(self,D):
		s = 0
		for word in self.words:
			s +=D.get(word,0)
		return s
	def modulo(self,lista):
		s = 0
		for k in lista:
			s += k*k		
		return sqrt(s)
	def count_vector(self,D):
		s = []
		for word in self.words:
			s.append(D.get(word,0))
		score = array(s).dot(self.weight)/self.modulo(s)
		return score
	def sort_by_count(self,d):  
    	#字典排序  
         d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))  
         return d
	def total_count_vector(self,datalist):
		score = dict()
		for database in datalist:
			data = load(open(database,'rb'))
			loca_s = dict()
			for name,D in data.items():
				s = self.count_vector(D)
				if s > self.n * 0.5:
					loca_s[name] = s
				else:
					pass
			score.update(loca_s)
		return self.sort_by_count(score)
	def total_count_sum(self,datalist):
		score = dict()
		for database in datalist:
			data = load(open(database,'rb'))
			loca_s = dict()
			for name,D in data.items():
				s = self.count_sum(D)
				if s > self.n * 0.5:
					loca_s[name] = s
				else:
					pass
			score.update(loca_s)
		return self.sort_by_count(score)
	def main(self,arg = 'vector'):
         datalist = self.data()
         if arg == 'vector':
         	score_dict = self.total_count_vector(datalist)
         	result_key = list(score_dict.keys())
         else:
         	score_dict = self.total_count_sum(datalist)
         	result_key = list(score_dict.keys())
         return result_key
def sen_query(sentence):
    start_time = clock()
    query_one = dealquery(sentence)
    result = query_one.main()
    end_time = clock()
    print(query_one.words)
    use_time = end_time - start_time
    print('查询 ',sentence ,'时共用时',str(use_time)+'s')
    return result
sentence_list = ['上市公司证券发行管理办法','奶奶级妈妈现在很流行',
					'男人的11个理由','皇帝“金口”吓走奇才','山崖牡丹成“天下第一奇花”','“高学费对穷人有好处”的逻辑悖谬和风险系数',
					'情绪的钟摆效应','世界第九大奇迹：新西兰萤火虫洞','美军在欧洲部署的B61型核弹']		
#result_d =dict()
#for sentence in sentence_list:
#	result_d[sentence] = sen_query(sentence)
#from pickle import dump
#dump(result_d,open('查询结果返回的列表.pickle','wb'))
sen_query('男人的11个理由')