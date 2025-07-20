import pandas as pd
import matplotlib.pyplot as plt

def Display():
    Data = pd.DataFrame({'Name': ['Amit', 'Sagar', 'Pooja'],'Math': [85, 90, 78],'Science': [92, 88, 80],'English': [75, 85, 82] })

    Data.set_index('Name', inplace=True)

    amit_marks = Data.loc['Amit']

    plt.plot(amit_marks.index, amit_marks.values, label='Amit')
    plt.title("Amit's Marks in all Subjects")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    Display()

if __name__ == "__main__":
    main()

