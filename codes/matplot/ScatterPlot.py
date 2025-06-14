# scatter plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  x = np.random.randint(1,50,20)
  y = np.random.randint(1,50,20)
  plt.scatter(x,y,color='c',linewidth=3)
  plt.xlabel("X Values")
  plt.ylabel("Y Values")
  plt.title("My First Line Plot")
  plt.show()

if __name__ == "__main__":
    main()