import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  df = pd.read_csv("../heatmap/sales_data.csv")
  data = df.groupby("Product Category")["Total Revenue"].sum()
  # Revenue over time
  df['Date'] = pd.to_datetime(df['Date'])
  plt.figure(figsize=(10,5))
  #plt.plot(df['Date'],df['Total Revenue'], marker='o')
  plt.hist(df['Total Revenue'], bins=25 , edgecolor='black')
  plt.xlabel('Total Revenue')
  plt.ylabel('Frequency')
  plt.title('Distribution of Total Revenue')
  plt.show()
  plt.show()
if __name__ == "__main__":
    main()