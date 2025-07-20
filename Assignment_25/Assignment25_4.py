import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def Display():

    data = pd.DataFrame({'Department':['HR','IT','Finance','HR','IT']})
    encoder = OneHotEncoder(sparse_output=False)
    encoded_data = encoder.fit_transform(data[['Department']])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Department']))
    print(encoded_df)






def main():
    Display()

if __name__ == "__main__":
    main()        