import pandas as pd
# Pandas dataframe can be used for multidimensional data
def main():
    # dictionary
    data = [
        {'Name':'Amal','Age':20,'Address':'Noida'},
        {'Name':'John','Age':21,'Address':'New York'},
        {'Name':'Rahul','Age':22,'Address':'Mumbai'},
    ]
    df = pd.DataFrame(data)
    print(df)
    # printing any specific column
    print("Printing only Address")
    df1 = df['Address']
    print(df1)

if __name__ == "__main__":
    main()