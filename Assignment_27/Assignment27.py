import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score , mean_squared_error


def AdvertisingLinearRegression(datasetpath):

    df = pd.read_csv(datasetpath)

    print("Initial data is:")
    print(df.head())

    print("Clean the dataset:")
    df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Updated data is:")
    print(df.head())

    print("Statistical data is:")
    print(df.describe())

    print("Correlation between features and labels/features and features:")
    print(df.corr())

    plt.figure(figsize=(8,8))
    sns.heatmap(df.corr(),annot= True,cmap='coolwarm')
    plt.title("correlation heatmap")
    plt.show()

    sns.pairplot(df)
    plt.suptitle("Pairplot if the dataset",y=1.02)
    plt.show()

    x = df[['TV','radio','newspaper']]
    y = df['sales']

    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42) 

    model = LinearRegression() 

    model.fit(x_train,y_train) 

    y_pred = model.predict(x_test) 

    mse = mean_squared_error(y_test,y_pred) 
    rmse = np.sqrt(mse) 
    r2 = r2_score(y_test,y_pred)                                

    
    print("mean square error is:",mse)      
    print("root mean square error is:",rmse)   
    print("r2 score is:",r2)  

    print("Model coefficient are:")
    for col , coef in zip(x.columns,model.coef_):
        print(f'{col}:{coef}')

    print("y intercept is:",model.intercept_)

    plt.figure(figsize=(8,6))
    plt.title("Actual vs Predicted sales")
    plt.scatter(y_test,y_pred,color='blue')
    plt.xlabel("Actual sales")
    plt.ylabel("Predicted sales")
    plt.grid(True)
    plt.show()                         
    

def main():
    AdvertisingLinearRegression("Advertising.csv")

if __name__ == "__main__":
    main()