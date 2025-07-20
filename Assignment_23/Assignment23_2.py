import pandas as pd

def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],'Math':[85,90,78],'Science':[92,88,80],'English':[75,85,82]})

    print("Statistical information of the dataset is:")
    print(Data.describe())

    

def main():
    Display()

if __name__ == "__main__":
    main()    
