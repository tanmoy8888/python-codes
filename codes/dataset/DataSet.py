import pandas as pd
# Pandas dataet
def main():
  df = pd.read_csv('sales_data.csv')
  print(df)
  print("--------------Printing first five rows----------------")
  print(df.head())

  print("--------------Printing last five rows----------------")
  print(df.tail())

if __name__ == "__main__":
    main()