# Histogram plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  x = [1,2,3,4,5]
  y = [10,20,30,40,50]
  z = [6,7,8,9,10]
  # Plot 1
  plt.subplot(1,2,1)
  plt.plot(x,y,color='red')
  # Plot 2
  plt.subplot(1,2,2)
  plt.plot(x,z,color='blue')
  plt.show()
if __name__ == "__main__":
    main()