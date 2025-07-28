import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score ,confusion_matrix

def winePredictorLogisticRegression(datasetpath):

    df = pd.read_csv(datasetpath)

    print("Initial data of the dataset:")
    print(df.head())

    print("Statistical data:")
    print(df.describe())

    print("Correlation between features and labels:")
    print(df.corr())

    # Visual format of Correlation matrix
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
    plt.title("Correlation matrix")
    plt.show()

    # Assigning features and labels
    x = df.drop(columns='Class')
    y = df["Class"]

    x_train , x_test ,y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = LogisticRegression()
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_test,y_pred)
    confMatrix = confusion_matrix(y_test,y_pred)

    print("Accuracy is:",Accuracy*100)
    print("confusion matrix is:",confMatrix)




    



def main():
    winePredictorLogisticRegression('WinePredictor.csv')

if __name__ == "__main__":
    main()    