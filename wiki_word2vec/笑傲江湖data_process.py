#!/usr/bin/env python
# -*- coding: utf-8 -*-
#笑傲江湖数据预处理
import re
import jieba
#读取数据
def read_data():
    """
    对要训练的文本进行处理，最后把文本的内容的所有词放在一个列表中
    """
    #读取停用词
    stop_words = []
    with open('./data/StopWord_new.txt',"r",encoding="UTF-8") as f:
        line = f.readline()
        while line:
            stop_words.append(line[:-1])
            line = f.readline()
    stop_words = set(stop_words)
    print('停用词读取完毕，共{n}个词'.format(n=len(stop_words)))

    # 读取文本，预处理，分词，得到词典
    raw_word_list = []
    rules =  u"([\u4e00-\u9fff]+)" #只提取中文
    pattern =  re.compile(rules)
    with open('./data/笑傲江湖.txt',"r", encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\r","").replace("\n","").strip()
            if line == "" or line is None:
                continue
            line = ' '.join(jieba.cut(line))
            seg_list = pattern.findall(line)
            words_list = []
            for word in seg_list:
                if word not in stop_words:
                    words_list.append(word)
            with open('./data/分词后的笑傲江湖.txt', 'a', encoding='utf-8') as ff:
                if len(words_list) > 0:
                    line = ' '.join(words_list) + "\n"
                    ff.write(line) # 词汇用空格分开
                    ff.flush()
                    raw_word_list.extend(words_list)
    return raw_word_list

words = read_data()
print(len(words))
print(len(set(words)))