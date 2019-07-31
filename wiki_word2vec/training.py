# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def my_function():
    wiki_news = open('./data/reduce_zhiwiki.txt', 'r',encoding='utf-8')
    model = Word2Vec(LineSentence(wiki_news), sg=0,size=200, window=5, min_count=5, workers=6)
    model.save('./model/zhiwiki_news.word2vec')

if __name__ == '__main__':
    my_function()
