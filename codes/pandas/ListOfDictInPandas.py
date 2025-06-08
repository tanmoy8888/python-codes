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
    print("---------Printing only Address------------")
    df1 = df['Address']
    print(df1)
    print("---------Printing only first row------------")
    print(df.loc[0])
    print("---------Printing only Name column value of first row------------")
    print(df.loc[0, 'Name'])
    # iloc function on dataframe
    print("---------Printing using ioc function ------------")
    print(df.iloc[1, 2])
    # adding a column in dataframe
    df['salary'] =[100,200,300]
    print("---------Addition of a new column in existing DF ------------")
    print(df)
    # dropping a column in dataframe
    df.drop('salary',axis=1,inplace=True)
    print("---------Dropping of a new column in existing DF ------------")
    print(df)
    # dropping a row in dataframe
    df.drop(0, axis=0, inplace=True)
    print("---------Dropping of row in existing DF ------------")
    print(df)
    df['Age']= df['Age']+1
    print("---------Incrementing value of a column in existing DF ------------")
    print(df)

if __name__ == "__main__":
    main()