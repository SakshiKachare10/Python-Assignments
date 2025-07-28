import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score , confusion_matrix , f1_score , precision_score , recall_score

import matplotlib.pyplot as plt
import seaborn as sns

def DiabetesDecisionTree(datasetpath):

    df = pd.read_csv(datasetpath)

    print("Displaying first 5 rows in dataset:")
    print(df.head())

    print("Column Information:")
    print(df.info())

    print("Statistical data from dataset:")
    print(df.describe())

    print("Plotting boxplot of distribution of target variables(Outcome)")
    
    sns.boxplot(data=df)
    plt.title('distribution of target variables(Outcome)')
    plt.show()

    df.dropna(inplace=True)

    x = df.drop(columns=['Outcome'])
    y = df['Outcome']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)
    

    x_train , x_test , y_train , y_test = train_test_split(x_scale,y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier(max_depth=10)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)

    print("Accuracy is:",accuracy_score(y_test,y_pred)*100)
    print("Confusion matrix is:",confusion_matrix(y_test,y_pred))
    print("Precision score is :",precision_score(y_test,y_pred))
    print("Recall score is:",recall_score(y_test,y_pred))
    print("F1 score is:",f1_score(y_test,y_pred))

    sns.heatmap(confusion_matrix(y_test,y_pred),annot=True)
    plt.title("Confusion Matrix")
    plt.show()

    pd.DataFrame(y_pred, columns=['predictions']).to_csv('predictionDecisionTree.csv')

    
def main():

    DiabetesDecisionTree("diabetes.csv")


if __name__ == "__main__":
    main()  
