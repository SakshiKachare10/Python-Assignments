import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

def Display():

    data = pd.DataFrame({'Salary':[25000,27000,29000,31000,50000,100000]})

    Q1 = data['Salary'].quantile(0.25)
    Q3 = data['Salary'].quantile(0.75)
    IQR = Q3 - Q1

    outliers = data[(data['Salary'] < Q1 - 1.5*IQR) | (data['Salary'] > Q3 + 1.5*IQR)]
    print(outliers)




def main():
    Display()

if __name__ == "__main__":
    main()        