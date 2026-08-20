import pandas as pd
import numpy as np
import sklearn
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
class HOUSE_PRICE:
    #training_data=pd.DataFrame()
    #testing_data=pd.DataFrame()
    reg=LinearRegression()
    def __init__(self,dfs):
        self.X=df.iloc[:,1:]
        self.y=df.iloc[:,0]
        self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.2,random_state=42)
    def train(self):
        self.reg.fit(self.x_train,self.y_train)
        print("Training is complete")
    def accuracy(self):
        self.train_pred_val=self.reg.predict(self.x_train)
        self.test_pred_val=self.reg.predict(self.x_test)
        train_num,test_num=0,0
        train_den,test_den=0,0
        for j,k in zip(self.y_train,self.train_pred_val):
            train_num=train_num+(k-j)**2
            train_den=train_den+(j-np.mean(self.y_train))**2
        print("The model accuracy with seen data is",1-(train_num/train_den))
        for z,c in zip(self.y_test,self.test_pred_val):
            test_num=test_num+(z-c)**2
            test_den=test_den+(z-np.mean(self.y_test))**2
        print("The model accuracy with test data is",1-(test_num/test_den))
    def loss(self):
        train_loss,test_loss=0,0
        for j,k in zip(self.y_test,self.test_pred_val):
            test_loss=test_loss+(j-k)**2
        print("The model loss on unseen data is",np.sqrt(test_loss/len(self.y_test)))
        for j,k in zip(self.y_train,self.tra in_pred_val):
            train_loss=train_loss+(j-k)**2
        print("The model loss with seen data is",np.sqrt(train_loss/len(self.y_train)))

df=pd.read_csv('data (1).csv')
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
cities = df['city'].unique()
city_map = {}
for i, city in enumerate(cities):
    city_map[city] = i
df['city'] = df['city'].map(city_map)
df['country']=0
df=df.drop(columns=['date'])
obj=HOUSE_PRICE(df)
obj.train()
with open("MLR_Model.pkl","wb") as t:
    pickle.dump(obj.reg, t)