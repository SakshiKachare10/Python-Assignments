import pandas as pd

def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],'Math':[85,90,78],'Science':[92,88,80],'English':[75,85,82]})

    Science_score = Data[Data["Science"] > 85]
    print(Science_score)

    
def main():
    Display()

if __name__ == "__main__":
    main()    
