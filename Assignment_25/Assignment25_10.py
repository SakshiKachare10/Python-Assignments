import pandas as pd
from sklearn.model_selection import train_test_split


def SplitDataset():

    data={'Age':[25,20,45,35,22],'Salary':[50000,60000,80000,65000,45000],'Purchased':[1,0,1,0,1]}

    df = pd.DataFrame(data)

    x = df[['Age','Salary']] # features
    y = df['Purchased']   # label

    x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)
    
    print("Training dataset is:")
    print(x_train)

    print("Training dataset is:")
    print(y_train)

    print("Testing dataset is:")
    print(x_test)

    print("Testing dataset is:")
    print(y_test)


    

def main():
    SplitDataset()

if __name__ == "__main__":
    main()        