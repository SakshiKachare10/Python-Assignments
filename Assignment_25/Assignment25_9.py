import pandas as pd
import numpy as np

def UseWhere():

    data ={'Marks':[45,67,88,32,76]}

    df =pd.DataFrame(data)

    df.where(df['Marks'] > 50,other='Fail',inplace=True)
    print(df)

def main():
    UseWhere()

if __name__ == "__main__":
    main()    