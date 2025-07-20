import pandas as pd

def Display():

    data = pd.DataFrame({'Name':['A','B','C'],
                         'Age':[21.0,22.0,23.0]})
    data['Age']= data['Age'].astype(int)
    print(data)




def main():
    Display()

if __name__ == "__main__":
    main()        