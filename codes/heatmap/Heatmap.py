import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  x = np.random.rand(4,4)
  plt.imshow(x,cmap = 'hot',)
  plt.colorbar()
  plt.show()

if __name__ == "__main__":
    main()