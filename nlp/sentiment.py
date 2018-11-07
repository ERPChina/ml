from collections import defaultdict
import os
import re
import jieba
import codecs

"""
1. 文本切割，将句子切分为词语列表
"""

def sent2word(sentence):
    """
    Segment a sentence to words
    Delete stopwords
    """
    segList = jieba.cut(sentence)
    segResult = []
    for w in segList:
        segResult.append(w)

    stopwords = readLines('stop_words.txt')
    newSent = []
    for word in segResult:
        if word in stopwords:
            # print "stopword: %s" % word
            continue
        else:
            newSent.append(word)

    return newSent
