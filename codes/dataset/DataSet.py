import pandas as pd
# Pandas dataet
def main():
  df = pd.read_csv('sales_data.csv')
  print(df)

if __name__ == "__main__":
    main()