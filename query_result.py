# -*- coding: utf-8 -*-
# Windows python3.5
# Spyde2
__author__ = 'huaijun'
import os
from os import path
from pickle import load
import re
def load_txt(file):
    with open(file,'r',encoding = 'utf-8') as f_h:
        res = f_h.read()
    return res
rootdirs = os.getcwd()
text_dirs = path.join(rootdirs,'sample')
temp = path.join(rootdirs,'temp')
if not path.isdir(temp):
    os.mkdir(temp)	
result_file = path.join(rootdirs,'查询结果返回的列表.pickle')
result  = load(open(result_file,'rb'))
sentence_list = ['上市公司证券发行管理办法','奶奶级妈妈现在很流行',
					'男人的11个理由','皇帝“金口”吓走奇才','山崖牡丹成“天下第一奇花”','“高学费对穷人有好处”的逻辑悖谬和风险系数',
					'情绪的钟摆效应','世界第九大奇迹：新西兰萤火虫洞','美军在欧洲部署的B61型核弹']		
'''
for sen in sentence_list:
    temp_sen = path.join(temp,str(sen[:4]))
    if not path.isdir(temp_sen):
        os.mkdir(temp_sen)
    result_list = result.get(sen,0)
    for x in range(10):
        text = load_txt(path.join(text_dirs,result_list[x]))
        with open(path.join(temp_sen,'result_'+ str(x)+ '.txt'),'w',encoding = 'utf-8') as w_f:
            w_f.write(text)'''
sentence_re = ['上市公司证券发行管理办法','奶奶级妈妈现在很流行',
					'男人的11个理由','皇帝“金口”吓走奇才','山崖牡丹成|天下第一奇花','高学费对穷人有好处',
					'情绪的钟摆效应','世界第九大奇迹|新西兰萤火虫洞','美军在欧洲部署的B61型核弹']		
rootfolder = path.join(rootdirs,'sample')
dirs = os.listdir(rootfolder)
filedirs = [ele for ele in dirs if ele.startswith('C0')]
D_count = dict(zip(sentence_list,filedirs))
sen_n = []
for k, sen in enumerate(sentence_list):
    #fileurl = D_count.get(sen,0)
    #url = path.join(rootfolder,fileurl)
    #folderlist = os.listdir(url)
    s = sentence_re[k]
    #folderlist = [ele for ele in folderlist if ele.endswith('.txt')]
    folderlist = result.get(sen,0)
    n = 0
    for u in folderlist:
        text = load_txt(path.join(rootfolder,u))
        if re.search(s,text):
            n+=1
    sen_n.append(n)
sen_count = dict(zip(sentence_list,sen_n))
