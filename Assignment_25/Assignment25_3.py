import pandas as pd
from sklearn.preprocessing import LabelEncoder

def Display():

    data = pd.DataFrame({'City':['Pune', 'Mumbai', 'Delhi','Pune','Delhi']})
    
    label = LabelEncoder()
    data['city']= label.fit_transform(data['City'])
    print(data)

    



def main():
    Display()

if __name__ == "__main__":
    main()        