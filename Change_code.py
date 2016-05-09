# -*- coding: utf-8 -*-
# Windows python3.5
# Spyde2
__author__ = 'huaijun'
import os
from os import path
class Changecoding(object):
    """docstring for Changecoding
    由于下载的文件编码格式为ANSI编码，此代码为更改编码格式UTF-8；
    更改后文档存在sample文件夹下"""
    def __init__(self):
        super(Changecoding, self).__init__()
        self.rootdir = os.getcwd()
        self.folderdirs = path.join(self.rootdir,'Reduced')
        self.dirs = os.listdir(self.folderdirs)
    def load_txt(self,file):
        with open(file,'r') as f_h:
            res = f_h.read()
            #new = res.decode('gbk', 'ignore').encode('utf-8') 
            return res
    def changing(self):        
        filedirs = [ele for ele in self.dirs if ele.startswith('C0')]
        samplefolder = path.join(self.rootdir, 'sample')
        if not path.isdir(samplefolder):
            os.mkdir(samplefolder)
        with open(path.join(self.rootdir,'wrong_code.txt'),'a+') as log_f:
            for dir in filedirs:
                donedir = path.join(samplefolder,dir)
                if not path.isdir(donedir):
                    os.mkdir(donedir)
                fileurl = path.join(self.folderdirs,dir)
                sondirs = os.listdir(fileurl)
                for name in sondirs:
                    try:
                        text = self.load_txt(path.join(fileurl,name))
                        with open(path.join(donedir,name),'w',encoding = 'utf-8') as w_f:
                            w_f.write(text)
                    except (IOError, UnicodeDecodeError, FileNotFoundError):
                        log_f.write('错误的编码'+str(dir)+ str(name)+'\t')
