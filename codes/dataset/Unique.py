import pandas as pd
# Pandas dataset
def main():
  df = pd.read_csv('sales_data.csv')
  #printing specific value
  df1 = df['Region'].nunique()
  print(df1)


if __name__ == "__main__":
    main()