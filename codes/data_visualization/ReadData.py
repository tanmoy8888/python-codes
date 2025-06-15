import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  df = pd.read_csv("../heatmap/sales_data.csv")
  data = df.groupby("Product Category")["Total Revenue"].sum()
  print(data)

  plt.bar(data.index,data.values)
  plt.xlabel('Category')
  plt.xlabel('Revenue')

  plt.show()
if __name__ == "__main__":
    main()