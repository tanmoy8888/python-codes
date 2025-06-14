import pandas as pd
# Pandas dataset
def main():
  df = pd.read_csv('sales_data.csv')
  elect = df.groupby('Product Category')['Unit Price'].mean()
  print(elect['Electronics'])


if __name__ == "__main__":
    main()