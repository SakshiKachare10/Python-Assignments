import pandas as pd

def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82],
                         'Total':[253,260,242]})
    
    Count = 0
    Pass = Data[Data['Total']>250]
    print("Students passed:")
    print(Pass)
    Count += len(Pass)
    print(f"Total students passed : {Count}")


def main():
    Display()


if __name__ =="__main__":
    main()    



