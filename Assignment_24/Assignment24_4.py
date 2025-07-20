import pandas as pd
import matplotlib.pyplot as plt 


def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]})
    
    Data.set_index('Name',inplace=True)

    sagar_marks= Data.loc['Sagar']


    plt.figure(figsize=(4,4))
    plt.pie(sagar_marks.values, labels=sagar_marks.index, autopct='%1.1f%%',)
    plt.title("Sagar's Marks")
    plt.axis('equal')
    plt.show()




def main():
    Display()


if __name__ =="__main__":
    main()    