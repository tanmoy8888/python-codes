import pandas as pd
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  x = [1,2,3,4]
  y = [10,20,30,40]
  plt.figure(figsize=(6,6))
  # alpha = transparency
  plt.plot(x,y,color='c',linewidth=3,marker='o',markerfacecolor='blue',alpha=1)
  # For adding grid
  plt.grid()
  plt.xlabel("X Values")
  plt.ylabel("Y Values")
  plt.title("My First Line Plot")
  plt.show()

if __name__ == "__main__":
    main()