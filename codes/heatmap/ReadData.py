import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  df = pd.read_csv("sales_data.csv")
  df = df.head()
  print(df)
  print(df['Product Category'].value_counts())

if __name__ == "__main__":
    main()