import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Pandas dataset
def main():
  df = pd.read_csv("../../heatmap/sales_data.csv")
  #sns.histplot(df['Total Revenue'],bins=20)
  product_name_data=df.groupby("Product Name")["Total Revenue"].sum().sort_values(ascending=False).reset_index().head(10)
  sns.barplot(x="Product Name",y="Total Revenue",data=product_name_data)
  plt.show()
if __name__ == "__main__":
    main()