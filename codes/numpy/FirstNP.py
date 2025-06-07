import numpy as np
def main():
    data = np.array([1,2,3,4,00,5])
    min_val = np.min(data)
    max_val = np.max(data)
    normalization_array = (data-min_val)/(max_val-min_val)
    print("min_val" , min_val)
    print("max_val" , max_val)
    print("normalization_array" , normalization_array)
if __name__ == "__main__":
    main()