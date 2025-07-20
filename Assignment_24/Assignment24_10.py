import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]})
    
    
    sns.boxplot(Data['English'])
    plt.title("Boxplot of English Marks")
    plt.show()
  

def main():
    Display()


if __name__ =="__main__":
    main()    