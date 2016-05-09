# -*- coding: utf-8 -*-
# Windows python3.5
# Spyde2
__author__ = 'huaijun'
import os
from os import path
import re
import jieba
from pickle import dump, load

from Change_code import Changecoding
class cut_for_search():
	"""docstring for cut_for_search
    将编码后的文档做分词，并把分词后的结果dump到本地
    以单个文件为单位存储"""
	def __init__(self):
		super(cut_for_search, self).__init__()
		self.rootdir = os.getcwd()
		self.STOP_WORDS_LIST = self.load_txt(path.join(self.rootdir, 'stopwords_utf8.txt'))
		self.STOP_WORDS_LIST = set([re.sub('\n', '', item) for item in self.STOP_WORDS_LIST])
	def filter_stop(self,input_text):
	    for token in input_text:
	        if token not in self.STOP_WORDS_LIST:
	            yield token
	def cut_word(self,sent):
	    words = self.filter_stop(jieba.cut_for_search(sent))
	    return ' '.join(words)
	def load_txt(self,file):
	    with open(file,'r',encoding = 'utf-8') as f_h:
	        res = [line.encode('utf-8', 'ignore').decode('utf-8', 'ignore') for line in f_h]
	    return res
	def get_seg_word(self,fileurl):
	    with open(fileurl,'r',encoding = 'utf-8') as f:
	    	f_words = f.read()
	    seg_word = self.cut_word(f_words)
	    return seg_word
	def main_files(self):
         if not 'wrong_code.txt' in os.listdir(self.rootdir):
             change = Changecoding()
             change.changing()
         rootfolder = path.join(self.rootdir,'sample')
         dirs = os.listdir(rootfolder)
         filedirs = [ele for ele in dirs if ele.startswith('C0')]
         seg_folder = path.join(self.rootdir,'seg')
         if not path.isdir(seg_folder):
             os.mkdir(seg_folder)	    
         for f in filedirs:
             tempdir = path.join(rootfolder,path.join(str(f), 'temp'))
             if not path.isdir(tempdir):
                 os.mkdir(tempdir)
#             try:
#                files = load(open(path.join(tempdir, 'task_list.pickle'), 'rb'))
#                task_exist = True
#             except (IOError, NameError, FileNotFoundError):
#              	task_exist = False
#             if not task_exist:
             files = os.listdir(path.join(rootfolder,f))
             files = [path.join(f, x) for x in files if x.endswith('.txt') ]
             dump(files, open(path.join(tempdir, 'task_list.pickle'), 'wb'))
             seg_dict ={}
             for d in files:
              	f_url = path.join(rootfolder,d)
              	seg_dict[d] = self.get_seg_word(f_url)
             dump(seg_dict,open(path.join(seg_folder,'segdict_'+str(f)+'_.pickle'),'wb'))