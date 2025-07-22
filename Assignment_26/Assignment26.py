import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 
from sklearn.preprocessing import LabelEncoder

def PlayPredictorKNN(datasetpath):

    df = pd.read_csv(datasetpath)

    df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Dimension of dataframe is:",df.shape)
    print("Initial data is:")
    print(df.head()) 

    Encoder = LabelEncoder()

    df['Whether']= Encoder.fit_transform(df['Whether'])  
    df['Temperature'] = Encoder.fit_transform(df['Temperature'])


    x = df[['Whether','Temperature']]  # features 
    y = df['Play']                      # labels 

    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

    model = KNeighborsClassifier(n_neighbors=5)

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_test,y_pred)

    print("Accuracy is :",Accuracy*100)
    
def main():
    PlayPredictorKNN("PlayPredictor.csv")

if __name__ == "__main__":
    main()        