基于中文维基百科的词向量构建及可视化
详见博客：https://blog.csdn.net/weixin_40547993/article/details/97781179

主要包括三部分：数据预处理、word2vec词向量训练、可视化
第一步：
    数据预处理：data_pre_process .py 实现对中文语料的预处理 ; angconv.py 和 zh_wiki.py 是将繁体中文转简体中文的文件。

第二步：
    词向量训练：training.py 利用gensim工具包实现word2vec词向量
    词向量相似度测试：word2vec_simiarity.py 计算两词语相似度以及找出指定词语的近义词
    加载模型找出指定词的相似词并制成词云：WordCloud_visualization.py

第三步：
    wiki百科数据词向量可视化：wiki_word2vec_visualization.py  利用Sklearn中TSNE进行词向量的可视化


具体效果及步骤详解见我的博客：https://blog.csdn.net/weixin_40547993/article/details/97781179


另外：
    词向量可视化测试代码：visualization_test.py
    《笑傲江湖》数据预处理：笑傲江湖data_process.py
    《笑傲江湖》可视化：笑傲江湖visualization.py


注：数据和训练模型太大没有上传    wiki百科数据需自己去下载。


具体效果及步骤详解见我的博客：https://blog.csdn.net/weixin_40547993/article/details/97781179