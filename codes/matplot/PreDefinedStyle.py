import pandas as pd
import matplotlib.pyplot as plt
# Pandas dataset
def main():
  # Available styles for chart/graphs
  print(plt.style.available)
  # ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'petroff10', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']
  # To use it
  plt.style.use('dark_background')

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