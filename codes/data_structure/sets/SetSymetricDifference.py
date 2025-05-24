def check_set():
   my_set_1 = {1,2,3,4,4,5,5}
   my_set_2 = {5,6,6,7,8,9,10}
   # Symmetric Difference returns all the unique elements from both sets
   print(my_set_1.symmetric_difference(my_set_2))
def main():
    check_set()

if __name__ == "__main__":
    main()