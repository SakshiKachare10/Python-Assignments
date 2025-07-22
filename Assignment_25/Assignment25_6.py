import pandas as pd 
import numpy as np

def Display():
    data = {"Grade":['A+','B','A','C','B+']}

    df = pd.DataFrame(data)

    ReplaceValues = {'A+':'Excellent','A':'Very Good','B+':'Good','B':'Average','C':'Poor'}

    df['Grade'] = df['Grade'].replace(ReplaceValues)
    
    print(df)

def main():
    Display()


if __name__ == "__main__":
    main()    