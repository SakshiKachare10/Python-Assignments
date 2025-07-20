import pandas as pd

def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],'Math':[85,90,78],'Science':[92,88,80],'English':[75,85,82]})

    print("shape of dataframe is:",Data.shape)
    print("Columns of dataframne is",Data.columns)
    print("Data types of columns are:",Data.dtypes)
    


def main():
    Display()

if __name__ == "__main__":
    main()    