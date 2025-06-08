import pandas as pd
# Pandas dataet
def main():
  df = pd.read_csv('sales_data.csv')
  print(df)
  print("--------------Printing first five rows----------------")
  print(df.head())

  print("--------------Printing last five rows----------------")
  print(df.tail)
  print("--------------Printing number of rows and columns----------------")
  print(df.shape)
  print("--------------Printing info of rows and columns----------------")
  print(df.info)
  print("--------------Printing description of rows and columns----------------")
  print(df.describe())
  print("--------------Printing sum of rows and columns----------------")
  print(df.isnull().sum())

if __name__ == "__main__":
    main()