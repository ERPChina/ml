import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split  #这里是引用了交叉验证
#from sklearn.svm import SVR  # SVM中的回归算法
#from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
#from sklearn.linear_model import BayesianRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import numpy as np

source = 'CMIC3.csv'
data = pd.read_csv(source)
#print(len(data[data.time<5])/len(data))
data.drop(data[(data.time>50)].index.tolist(), inplace=True)


l=(data['length'] - data['length'].min()) / (data['length'].max()-data['length'].min())
h=(data['height'] - data['height'].min()) / (data['height'].max()-data['height'].min())
body=(data['bodyAngle'] - data['bodyAngle'].min()) / (data['bodyAngle'].max()-data['bodyAngle'].min())
jia=(data['wheelAngle'] - data['wheelAngle'].min()) / (data['wheelAngle'].max()-data['wheelAngle'].min())
h=(data['headAngle'] - data['headAngle'].min()) / (data['headAngle'].max()-data['headAngle'].min())
#t=(data['time'] - data['time'].min()) / (data['time'].max()-data['time'].min())
#以下代码将数据画图可以发现异常数据
#plt.hist(data['time'], 50)
#plt.scatter(data['length'],data['time'])
#plt.show()

data['length']=l
data['height']=h
data['bodyAngle']=body
data['wheelAngle']=jia
data['headAngle']=h
#data['time']=t
#print(data.corr()['time'])

feature_cols = ['height','bodyAngle','headAngle']
#feature_cols = ['height']
#feature_cols = ['length','height','bodyAngle','wheelAngle','headAngle']
X = data[feature_cols]
Y = data['time']

X_train,X_test, y_train, y_test = train_test_split(X, Y, random_state=1)
#PCA分析
#pca=PCA(n_components='mle',svd_solver='full')
#pca=PCA(n_components=3)
#newData=pca.fit_transform(np.array(X_train))
#print(pca.explained_variance_ratio_ )

#algorithm = RandomForestRegressor(n_estimators=1000,criterion='mse',random_state=1,n_jobs=1)
algorithm = GradientBoostingRegressor(n_estimators=80,max_depth=15) #BayesianRidge() #SVR()
#algorithm = LinearRegression();
#algorithm = DecisionTreeRegressor(max_depth=15)
model=algorithm.fit(X_train, y_train)
print(algorithm.score(X_train, y_train))
print(model)
#print(algorithm.intercept_)
#print(algorithm.coef_)
y_pred = algorithm.predict(X_test)

plt.figure()
plt.plot(range(len(y_pred)),y_test,'r',label="test")
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of Test Data")
plt.ylabel('value of Result')


sum_mean=0
for i in range(len(y_pred)):
    sum_mean+=(y_pred[i]-y_test.values[i])**2
sum_erro=np.sqrt(sum_mean/len(y_pred))
print(sum_erro)
# visualize the relationship between the features and the response using scatterplots
#sns.pairplot(data, x_vars=['length'], y_vars='time',  kind='scatter',size=6, aspect=0.8)
#plt.show()#注意必须加上这一句，否则无法显示。

plt.show()

#print(data.corr()['time'])
