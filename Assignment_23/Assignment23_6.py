import pandas as pd

def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],'Math':[85,90,78],'Science':[92,88,80],'English':[75,85,82]})

    mapping_dict = {'Amit':253,'Sagar':260,'Pooja':242}

    Data['Total'] = Data['Name'].map(mapping_dict)

    print(Data)
    
    Sorted_values = Data.sort_values('Total', ascending=False)
    print(Sorted_values)

def main():
    Display()

if __name__ == "__main__":
    main()    
