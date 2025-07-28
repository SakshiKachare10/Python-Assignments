import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score , confusion_matrix
 

def WinePredictorKNN(datasetpath):

    # get the dataset from csv
    df = pd.read_csv(datasetpath)

    print("Initial dataset is:")
    print(df.head())

    print("Statistical data is:")
    print(df.describe()) 

    print("Correlation matrix:")
    print(df.corr())

    # plot heatmap for correlation
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
    plt.title("Wine Predictor Correlation")
    plt.show()    

    # assigning features and target variable 
    x = df.drop(columns='Class')
    y = df['Class']

    x_train ,x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    
    AccuracyScoremain = []
    k_range = range(1,21)

    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        Accuracy = accuracy_score(y_test,y_pred)
        AccuracyScoremain.append(Accuracy)

    plt.figure(figsize=(8,6))
    plt.plot(k_range,AccuracyScoremain,marker = 'o',linestyle='--')
    plt.title("Value of k vs accuracy score") 
    plt.xlabel("Value of k")
    plt.ylabel("Accuracy")   
    plt.grid(True)
    plt.xticks(k_range)
    plt.show()

    best_k = k_range[AccuracyScoremain.index(max(AccuracyScoremain))]
    print("best k value aftter tuning is:",best_k)

    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    Accuracy = accuracy_score(y_test,y_pred)
    AccuracyScoremain.append(Accuracy)

    print("The best accuracy is:",Accuracy*100)
    CM = confusion_matrix(y_test,y_pred)
    print("The confusion matrix is:",CM)


def main():

    WinePredictorKNN("WinePredictor.csv")

if __name__ == "__main__":
    main()   