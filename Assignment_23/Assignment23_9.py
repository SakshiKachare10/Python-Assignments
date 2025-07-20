import pandas as pd
import numpy as np 

def Display():
    Data2 = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                          'Math':[np.nan,76,88],
                          'Science':[91,np.nan,85]})
    
  
    Data2[['Math', 'Science']] = Data2[['Math','Science']].fillna(Data2[['Math','Science']].mean())
    print(Data2)

def main():
    Display()

if __name__ == "__main__":
    main()    
