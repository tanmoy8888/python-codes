# Display only product name and total revenue where unit sold is less than 5
import pandas as pd
# Pandas dataset
def main():
  df = pd.read_csv('sales_data.csv')
  #printing specific value
  elect = df.groupby('Product Name')['Total Revenue'].sum().sort_values(ascending=False).head(3)
  print(elect)


if __name__ == "__main__":
    main()