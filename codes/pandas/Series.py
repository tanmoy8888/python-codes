import pandas as pd
def main():
    data = [1,2,3,4,5]
    # In pandas, it automatically creates an index in the data.
    # In Series of Pandas it can generate one dimensional series not multidimensional like numpy
    series_1 = pd.Series(data)
    print(series_1)
    # data with index in pandas series
    data = [1,2,3]
    index = ['a','b','c']
    series_2 = pd.Series(data, index)
    print(series_2)
if __name__ == "__main__":
    main()