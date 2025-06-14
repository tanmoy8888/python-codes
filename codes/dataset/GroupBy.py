import pandas as pd
# Pandas dataset
def main():
  df = pd.read_csv('sales_data.csv')
  #printing specific value
  df1 = df[df['Region'] == 'North America']
  print(df1)


if __name__ == "__main__":
    main()