# -*- coding:utf-8 -*-
__author__ = 'patrick.li@sap.com'
import jieba
import jieba.posseg as pseg

text='大金空调是一个世界知名品牌，是一个集科研、制造为一体的空调生产厂家。大金生产的压缩机也是很出名的，世界好多空调厂家，包括国内知名品牌的空调厂家，在高端机型上都是用的大金压缩机。在实际维修中，该品牌空调也很少出问题，质量非常不错，不过价格上要比国内品牌高一些。'

seg_list = jieba.cut(text)
print(','.join(seg_list))
words = pseg.cut(text)
for word, flag in words:
    print('%s %s' % (word, flag))
