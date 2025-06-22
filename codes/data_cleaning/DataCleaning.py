import pandas as pd
import numpy as np
# Pandas dataset
def main():
  df = pd.read_excel("../../data/flight_price.xlsx")
  print(df)
  df.dropna(subset=['Route','Total_Stops'],inplace=True)
  print(df.isnull().sum())

  # Unique values
  print(df['Airline'].value_counts())
  # Splitting date
  print(df['Date_of_Journey'].str.split('/'))
  # Taking only date
  df['Days'] = df['Date_of_Journey'].str.split('/').str[0]
  print(df['Days'])
  ## Not working need to fix
  #print(df['Duration'].str.split(" ").str[0].split('h').str[0].astype(int))




if __name__ == "__main__":
    main()