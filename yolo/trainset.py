import os
import random

trainval_percent = 0.9
train_percent = 8/9
num=30
xmlfilepath = './dataset/Annotations'
txtsavepath = './dataset/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

#num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent) #27
tr=int(tv*train_percent)    #18
trainval= random.sample(list,tv)  #
train=random.sample(trainval,tr)

ftrainval = open(txtsavepath+'/trainval.txt', 'w')
ftest = open(txtsavepath+'/test.txt', 'w')
ftrain = open(txtsavepath+'/train.txt', 'w')
fval = open(txtsavepath+'/val.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
