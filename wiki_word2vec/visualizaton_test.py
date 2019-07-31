#!/usr/bin/python
# -*- coding: UTF-8 -*-
#可视化测试
"""
@author:Administrator
@file:visualizaton_test.py
@time:2019/07/30
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Administrator
@file:wiki_word2vec_visualization.py
@time:2019/07/30
"""

import pandas as pd
pd.options.mode.chained_assignment = None
import numpy as np
import re
import nltk
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import logging
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

wiki_news = open('./data/P1_keywords.txt', 'r',encoding='utf-8')
model = Word2Vec(LineSentence(wiki_news), sg=0,size=50, window=10, min_count=1)
print('model训练完成')

def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []
    print(11111111111)
    for word in model.wv.vocab:
        tokens.append(model[word])
        labels.append(word)

    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)
    print(222222222)
    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    plt.figure(figsize=(16, 16))
    print(333333333)
    for i in range(len(x)):
        plt.scatter(x[i], y[i])
        plt.annotate(labels[i],
                     fontproperties=font,
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()

# model = './model/zhiwiki_news.word2vec'
tsne_plot(model)