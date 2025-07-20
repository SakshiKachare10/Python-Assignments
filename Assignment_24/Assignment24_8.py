import pandas as pd
import matplotlib.pyplot as plt


def Display():
    Data = pd.DataFrame({'Name':['Amit','Sagar','Pooja'],
                         'Math':[85,90,78],
                         'Science':[92,88,80],
                         'English':[75,85,82]})


    plt.figure(figsize=(10, 5))
    plt.hist(Data['Math'],color='green',edgecolor ='black')
    plt.title("Math Marks")
    plt.xlabel("Marks")
    plt.ylabel("Range")
    plt.grid(True)
    plt.show()
                            
def main():
    Display()


if __name__ =="__main__":
    main()    