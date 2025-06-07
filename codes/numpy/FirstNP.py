import numpy as np
def main():
    data = np.array([1,2,3,4,00,5])
    min_val = np.min(data)
    max_val = np.max(data)
    std_val = np.std(data)
    normalization_array = (data-min_val)/(max_val-min_val)
    normalization_array_std_deviation = (data-min_val)/std_val
    print("min_val" , min_val)
    print("max_val" , max_val)
    print("std_val" , std_val)
    print("normalization_array" , normalization_array)
    print("normalization_array_std_deviation" , normalization_array_std_deviation)
if __name__ == "__main__":
    main()