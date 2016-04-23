# -*- coding: utf-8 -*-
# Windows python3.5
# Spyde2
__author__ = 'huaijun'
import os
import collections
from os import path
from pickle import load
from time import clock

from segword import cut_for_search
from FitTfidf import TFIDF
class dealquery(object):
	"""docstring for dealquery"""
	def __init__(self, sentence):
		super(dealquery, self).__init__()
		self.sentence = sentence
		self.rootdir = os.getcwd()
		self.words = self.cut_seg()
	def data(self):
		dataurl = path.join(self.rootdir,'database')
		datadir = os.listdir(dataurl)
		datadirurl = [path.join(dataurl,ele) for ele in datadir if ele.startswith('C0') and ele.endswith('.pickle')]	
		return datadirurl		
	def cut_seg(self):
		cut = cut_for_search()
		words = cut.cut_word(self.sentence)
		wordlist = words.split(' ')
		return wordlist
	def count(self,D):
		s = 0
		for word in self.words:
			s +=D.get(word,0)
		return s
	def sort_by_count(self,d):  
    	#字典排序  
         d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))  
         return d
	def total_count(self,datalist):
		score = dict()
		for database in datalist:
			data = load(open(database,'rb'))
			loca_s = dict()
			for name,D in data.items():
				loca_s[name] = self.count(D)
			score.update(loca_s)
		return self.sort_by_count(score)
	def main(self):
         datalist = self.data()
         score_dict = self.total_count(datalist)
		#re设定返回的阈值 
         result_key = list(score_dict.keys())
         return score_dict

start_time = clock()
sentence = '皇帝“金口”吓走奇才'
query_one = dealquery(sentence)
result = query_one.main()
end_time = clock()
print('查询共用时',str(end_time-start_time)+'s')

		
