'''
House Price Prediction using Multiple Linear Regression

This module implements a house price prediction system using
Multiple Linear Regression with scikit-learn.

The project includes:
- Data preprocessing and feature extraction from the date column
- Encoding of city and country information
- Splitting the dataset into training and testing sets
- Training a Multiple Linear Regression model
- Evaluating model performance using R² score and RMSE
- Saving the trained model using Pickle
- Loading the saved model and making predictions on custom inputs
'''
import pandas as pd
import numpy as np
import sklearn
import sys
import pickle
import warnings
warnings.filterwarnings("ignore")
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
class HOUSE_PRICE:

    def __init__(self,dfs):
        try:
            dfs['date'] = pd.to_datetime(dfs['date'])
            dfs['year'] = dfs['date'].dt.year
            dfs['month'] = dfs['date'].dt.month
            dfs['day'] = dfs['date'].dt.day
            cities = dfs['city'].unique()
            city_map = {}
            for i, city in enumerate(cities):
                city_map[city] = i
            dfs['city'] = dfs['city'].map(city_map)
            dfs['country'] = 0
            dfs = dfs.drop(columns=['date'])
            self.X=dfs.iloc[:, 1:]
            self.y=dfs.iloc[:,0]
            self.x_train,self.x_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.2,random_state=42)
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no : {er_line.tb_lineno} : due to : {er_msg} : reason : {er_ty}")

    def train(self):
        try:
            self.reg=LinearRegression()
            self.reg.fit(self.x_train,self.y_train)
            print("Training is complete")
            self.training=pd.DataFrame()
            self.testing=pd.DataFrame()
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
    def accuracy(self):
        try:
            self.train_pred_val=self.reg.predict(self.x_train)
            self.test_pred_val=self.reg.predict(self.x_test)
            self.training["y_train"]=self.y_train.copy()
            self.training["y_predict"]=self.train_pred_val.copy()
            self.testing["y_test"]=self.y_test.copy()
            self.testing["y_tpredict"]=self.test_pred_val.copy()
            train_num,test_num=0,0
            train_den,test_den=0,0
            for i in self.training.index:
                train_num=train_num+(self.training["y_train"][i]-self.training["y_predict"][i])**2
                train_den=train_den+(self.training["y_train"][i]-np.mean(self.y_train))**2
            print("The model accuracy with seen data is",1-(train_num/train_den))
            for j in self.testing.index:
                test_num=test_num+(self.testing["y_test"][j]-self.testing["y_tpredict"][j])**2
                test_den=test_den+(self.testing["y_test"][j]-np.mean(self.y_test))**2
            print("The model accuracy with test data is",1-(test_num/test_den))
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
    def loss(self):
        try:
            train_loss,test_loss=0,0
            for i in self.training.index:
                train_loss=train_loss+(self.training["y_train"][i]-self.training["y_predict"][i])**2
            print("The model loss on seen data is",np.sqrt(train_loss/len(self.y_train)))
            for j in self.testing.index:
                test_loss=test_loss+(self.testing["y_test"][j]-self.testing["y_tpredict"][j])**2
            print("The model loss with unseen data is",np.sqrt(test_loss/len(self.y_test)))
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
    def modelfile(self):
        try:
            with open("MLR_Model.pkl", "wb") as t:
                pickle.dump(obj.reg, t)
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()

    def custom_inputs(self):
        try:
            with open("MLR_Model.pkl", "rb") as f:
                m = pickle.load(f)
            prediction = m.predict([[3, 1.5, 1340, 7912, 1.5, 0, 0, 3, 1340, 0, 1955, 2005, 36, 0, 2014, 5, 2]])
            print("prediction:", prediction[0])
        except Exception as e:
            er_ty, er_msg, er_line = sys.exc_info()
            print(f"Error in line no : {er_line.tb_lineno} : due to : {er_msg} : reason : {er_ty}")

if __name__ == "__main__":
    df=pd.read_csv('data.csv')
    obj=HOUSE_PRICE(df)
    obj.train()
    obj.accuracy()
    obj.loss()
    obj.modelfile()
    obj.custom_inputs()
