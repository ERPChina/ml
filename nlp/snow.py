from snownlp import SnowNLP
# SnowNLP库：
# words：分词
# tags：关键词
# sentiments：情感度
# pinyin：拼音
# keywords(limit)：关键词
# summary：关键句子
# sentences：语序
# tf：tf值
# idf：idf值
s = SnowNLP(u'大金空调是一个世界知名品牌，是一个集科研、制造为一体的空调生产厂家。大金生产的压缩机也是很出名的，世界好多空调厂家，包括国内知名品牌的空调厂家，在高端机型上都是用的大金压缩机。在实际维修中，该品牌空调也很少出问题，质量非常不错，不过价格上要比国内品牌高一些。')
# s.words         # [u'这个', u'东西', u'真心', u'很', u'赞']
print(s.words)
print(s.keywords(6))  # [u'语言', u'自然', u'计算机'] 不能用tags输出关键字.
print(s.summary(3))  # [u'
print(s.sentiments)


