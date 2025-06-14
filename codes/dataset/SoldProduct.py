# Display only product name and total revenue where unit sold is less than 5
import pandas as pd
# Pandas dataset
def main():
  df = pd.read_csv('sales_data.csv')
  #printing specific value
  elect = df[df['Units Sold'] <5][['Product Name','Total Revenue']]
  print(elect)


if __name__ == "__main__":
    main()