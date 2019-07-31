#coding=utf-8
#相似度
import gensim
import pandas as pd
def my_function():

    model = gensim.models.Word2Vec.load('./model/zhiwiki_news.word2vec')
    print(model.similarity('西红柿','番茄'))  #相似度为0.60256344
    print(model.similarity('西红柿','香蕉'))  #相似度为0.49495476
    # print(model.similarity('人工智能','大数据'))
    # print(model.similarity('滴滴', '共享单车'))

    result = pd.Series(model.most_similar(u'阿里巴巴'))
    print(result)
    result1 = pd.Series(model.most_similar(u'故宫'))
    print(result1)
    print(model.wv['中国'])
if __name__ == '__main__':
    my_function()

# word = '中国'
# if word in model.wv.index2word:
#     print(model.most_similar(word))
