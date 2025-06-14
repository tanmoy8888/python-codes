import pandas as pd
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  x = ['A','B','C','D']
  y = [10,20,30,40]
  plt.bar(x,y,color='c',linewidth=3)
  plt.xlabel("X Values")
  plt.ylabel("Y Values")
  plt.title("My First Line Plot")
  plt.show()

if __name__ == "__main__":
    main()