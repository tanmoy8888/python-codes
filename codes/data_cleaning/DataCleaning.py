import pandas as pd
import numpy as np
# Pandas dataset
def main():
  df = pd.read_excel("../../data/flight_price.xlsx")
  print(df)
  df.dropna()
if __name__ == "__main__":
    main()