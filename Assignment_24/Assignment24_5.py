import pandas as pd

def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82],
                         'Total':[253,260,242]})
    
    Pass = Data[Data['Total']>250]
    print("Students passed:")
    print(Pass)

    Fail= Data[Data['Total']<250]
    print("Students failed:")
    print(Fail)
   

def main():
    Display()


if __name__ =="__main__":
    main()    



