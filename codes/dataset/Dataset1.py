import pandas as pd
# Pandas dataet
def main():
  df = pd.read_csv('sales_data.csv')
  #printing specific value
  df1 = df[df['Region'] == 'Europe']
  print(df1)

if __name__ == "__main__":
    main()