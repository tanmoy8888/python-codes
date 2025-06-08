import pandas as pd
def main():
    data = [1,2,3,4,5]
    # In pandas, it automatically creates an index in the data.
    # In Series of Pandas it can generate one dimensional series not multidimensional like numpy
    series = pd.Series(data)
    print(series)
if __name__ == "__main__":
    main()