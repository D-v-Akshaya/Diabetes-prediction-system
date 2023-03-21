#Importing the required modules
import pandas as pd
import numpy as np
#from scipy.sparse.construct import random
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model  import LogisticRegression
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.naive_bayes  import GaussianNB
from sklearn.svm  import SVC
from sklearn.tree  import DecisionTreeClassifier
from sklearn.ensemble  import RandomForestClassifier
class Data_analysis:
    dia=pd.read_csv(r'diabetes.csv')
    #Exploring the data analysis
    #Understanding the dataset
    def analysis (self):
        print(self.dia.head())
        print(self.dia.shape)
        print(self.dia.info())
        print(self.dia.describe())
        print(self.dia.isnull().values.any())
        

    #After understanding the data we  now know that columns Glucose ,BloodPressure, SkinThickness , Insulin and BMI shouldnot have 0 values 
    #so checking the no. of zeroes in the dataset
    #print(dia[dia['Glucose']==0].shape[0])
    #print(dia[dia['BloodPressure']==0].shape[0])
    #print(dia[dia['SkinThickness']==0].shape[0])
    #print(dia[dia['Insulin']==0].shape[0])               
    #print(dia[dia['BMI']==0].shape[0])
    #Data cleaning    
    dia=dia.drop_duplicates()    #Droping any duplicate value
    #After checking we are replacing it with mean of the column
    #dia['Glucose']=dia['Glucose'].replace(0,dia['Glucose'].mean())
    #dia['BloodPressure']=dia['BloodPressure'].replace(0,dia['BloodPressure'].mean())
    #dia['SkinThickness']=dia['SkinThickness'].replace(0,dia['SkinThickness'].mean())
    #dia['Insulin']=dia['Insulin'].replace(0,dia['Insulin'].mean())
    #dia['BMI']=dia['BMI'].replace(0,dia['BMI'].mean())

    #Data visulalisation

    #Count ploting the dependent data
    def pie(self):
        f,ax=plt.subplots(1,figsize=(10,5))
        self.dia['Outcome'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
        ax[0].set_title('Outcome')
        ax[0].set_ylabel(' ')
        #sns.countplot('Outcome',data=self.dia,ax=ax[1])
        #ax[1].set_title('Outcome')
        N,P=self.dia['Outcome'].value_counts()
        print('negative(0) :',N)
        print('positive(1) :',P)
        plt.grid()
        return plt.show()
    ##Histogram of the  data set
    def hist(self):
        self.dia.hist(bins=10,figsize=(10,10))
        return plt.show()
    ##Pair ploting
    def pair_plot(self):
        sns.pairplot(data=self.dia,hue='Outcome')
        return plt.show()
    ##Analizing the data set and the dependent valriables
    def correlation(self):
        cor=self.dia.corr()
        cor_index=cor.index
        plt.figure(figsize=(10,10))
        g=sns.heatmap(self.dia[cor_index].corr(),annot=True,cmap="Blues")
        return plt.show()

    #Understanding the dependent variable 
    #print(dia['Outcome'].value_counts())
    #print(dia.groupby('Outcome').mean())
    #dividing the dataset into acorrding to the independent and dependent variables
    y=dia['Outcome']
    _x_=dia.drop(columns='Outcome',axis=1)
    #standerdizing the independent variables
    scaler=StandardScaler()
    scaler.fit(_x_)
    x=scaler.transform(_x_)
    #spliting the dataset in to training and testing set
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,stratify=y,random_state=7)
    

    #training the model
    #  Seleting_model(Spliting):
    #logical regression
    def seleting_model(self):
        lr=LogisticRegression(solver='liblinear',multi_class='ovr')
        lr.fit(self.xtrain,self.ytrain)
        #kNeighbors classifier(KNN)
        knn=KNeighborsClassifier()
        knn.fit(self.xtrain,self.ytrain)
        #Navi bayes classifier
        nb=GaussianNB()
        nb.fit(self.xtrain,self.ytrain)
        #support vector machine(svm)
        svm=SVC()
        svm.fit(self.xtrain,self.ytrain)
        #Decision tree
        dt=DecisionTreeClassifier()
        dt.fit(self.xtrain,self.ytrain)
        #Random forest
        rf=RandomForestClassifier()
        rf.fit(self.xtrain,self.ytrain)
        
        #Model Evaluation
        print("Training set Accuracy ")
        #logical regression
        train_accuracy_lr=accuracy_score(lr.predict(self.xtrain),self.ytrain)
        print('Logical regression =',train_accuracy_lr*100)
        #kNeighbors classifier(KNN)
        train_accuracy_knn=accuracy_score(knn.predict(self.xtrain),self.ytrain)
        print('KNeighbors Classifier =',train_accuracy_knn*100)
        #Navi bayes classifier
        train_accuracy_nb=accuracy_score(nb.predict(self.xtrain),self.ytrain)
        print('Navi Bayes =',train_accuracy_nb*100)
        #support vector machine(svm)
        train_accuracy_svm=accuracy_score(svm.predict(self.xtrain),self.ytrain)
        print('Support vector Machine =',train_accuracy_svm*100)
        #Decision tree
        train_accuracy_dt=accuracy_score(dt.predict(self.xtrain),self.ytrain)
        print('Decision Tree =',train_accuracy_dt*100)
        #Random forest
        train_accuracy_rf=accuracy_score(rf.predict(self.xtrain),self.ytrain)
        print('Random Forest =',train_accuracy_rf*100)
        
        #Accuracy score evalution
        print("Testing the Accuracy")
        #logical regression
        test_accuracy_lr=accuracy_score(lr.predict(self.xtest),self.ytest)
        print('Logical regression =',test_accuracy_lr*100)
        #kNeighbors classifier(KNN)
        test_accuracy_knn=accuracy_score(knn.predict(self.xtest),self.ytest)
        print('KNeighbors Classifier =',test_accuracy_knn*100)
        #Navi bayes classifier
        test_accuracy_nb=accuracy_score(nb.predict(self.xtest),self.ytest)
        print('Navi Bayes =',test_accuracy_nb*100)
        #support vector machine(svm)
        test_accuracy_svm=accuracy_score(svm.predict(self.xtest),self.ytest)
        print('Support Vector Machine =',test_accuracy_svm*100)
        #Decision tree
        test_accuracy_dt=accuracy_score(dt.predict(self.xtest),self.ytest)
        print('Decision Tree =',test_accuracy_dt*100)
        #Random forest
        test_accuracy_rf=accuracy_score(rf.predict(self.xtest),self.ytest)
        print('Random Forest =',test_accuracy_rf*100)
        print(f'The Accuracy of Random Forest model is {test_accuracy_lr*100} , higher so for this dataset we are going to use Logical Regression model ')
    #making predictive system
    def predicte(self,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
        dia=pd.read_csv(r'diabetes.csv')
        y=dia['Outcome']
        _x_=dia.drop(columns='Outcome',axis=1)
        scaler=StandardScaler()
        scaler.fit(_x_)
        x=scaler.transform(_x_)
        xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,stratify=y,random_state=7)
        lr=LogisticRegression(solver='liblinear',multi_class='ovr')
        lr.fit(self.xtrain,self.ytrain)
        test_accuracy_lr=accuracy_score(lr.predict(xtest),ytest)
        indata=(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        inarray=np.array(indata)
        inreshape=inarray.reshape(1,-1)
        instd=scaler.transform(inreshape)
        return lr.predict(instd)
if __name__ =='__main__':
    d=Data_analysis()
    #d.predicte(6,148,72,35,0,33.6,0.627,50)
    #d.analysis()
    #d.pie()
    #d.hist()
    d.pair_plot()
    #d.correlation()
    #d.seleting_model()