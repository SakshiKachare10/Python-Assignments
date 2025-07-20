import pandas as pd
from sklearn.preprocessing import MinMaxScaler  

def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]})
    
    scalar = MinMaxScaler()
    Data[['Math']] = scalar.fit_transform(Data[['Math']])

    print(Data)

def main():
    Display()


if __name__ =="__main__":
    main()    