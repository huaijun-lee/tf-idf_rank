# tf-idf_rank
毕业论文，基于TF-IDF的文本排序;
chang_code 更改原先文本的编码格式，改为更适合分词的utf-8编码;
segword 用于分词，并将每一个文件夹下的分词结果以字典的形式存储，其key为文件名，并把每个字典dump到本地存储.
fit_idf 计算全部文档（即该语料库）的IDF值，并以dict形式dump到本地;
FitTfIdf 计算各文档的TF-IDF值；
mydatebase用于将文档的TF-IDF值保存至ZODB关系数据库中；
query用于查询
