import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def Display():

    data = {'Age':[18,22,25,30,35]}

    df = pd.DataFrame(data)

    scaler = MinMaxScaler()
    df[['Age']] = scaler.fit_transform(df[['Age']])

    print(df)


def main():
    Display()

if __name__ == "__main__":
    main() 