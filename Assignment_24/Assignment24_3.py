import pandas as pd


def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                         'Gender':['Male','Male','Female'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]})
    
    avg_marks = Data.groupby('Gender')[['Math','Science','English']].mean()

    print(avg_marks)
    
def main():
    Display()


if __name__ =="__main__":
    main()    