import pandas as pd
# Pandas dataframe can be used for multidimensional data
def main():
    # dictionary
    data = {'name':['Amal',"John","krish"],
            'age': [24,15,16],
            'City':['Noida','New York','Florida']
            }
    df = pd.DataFrame(data)
    print(df)

if __name__ == "__main__":
    main()