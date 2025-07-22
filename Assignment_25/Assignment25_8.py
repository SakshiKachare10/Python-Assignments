import pandas as pd
import numpy as np


def InterpolateMethod():
    data = {'Marks':[85,np.nan,90,np.nan,95]}

    df = pd.DataFrame(data)

    marks_interpolate = df.interpolate()
    print(marks_interpolate)

def main():
    InterpolateMethod()

if __name__ == "__main__":
    main() 