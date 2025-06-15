import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Pandas dataset
def main():
  df = pd.read_csv("../heatmap/sales_data.csv")
  sns.histplot(df['Total Revenue'],bins=20)
  plt.show()
if __name__ == "__main__":
    main()