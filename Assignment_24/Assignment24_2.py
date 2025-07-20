import pandas as pd
from sklearn.preprocessing import OneHotEncoder 


def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                         'Gender':['Male','Male','Female'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]})
    
    Encoder = OneHotEncoder(sparse_output=False)
    Gender_encoded = Encoder.fit_transform(Data[['Gender']])
    Gender_column = Encoder.get_feature_names_out(['Gender'])
    Gender_data = pd.DataFrame(Gender_encoded,columns=Gender_column)

    final_data = pd.concat([Data.drop('Gender',axis=1),Gender_data],axis=1)
    print(final_data)

def main():
    Display()


if __name__ =="__main__":
    main()    

