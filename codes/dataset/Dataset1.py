import pandas as pd
# Pandas dataset
def main():
  df = pd.read_csv('sales_data.csv')
  #printing specific value
  df1 = df[df['Region'] == 'Europe']
  print(df1)
  # sorting on a specific column
  df2 = df.sort_values(by='Total Revenue' , ascending=False)
  print("----------Printing in sorted order-------------")
  print(df2)
  # group by
  print("----------Printing sum of revenue based on the region-------------")
  df3 = df.groupby('Region')['Total Revenue'].sum()
  print(df3)

if __name__ == "__main__":
    main()