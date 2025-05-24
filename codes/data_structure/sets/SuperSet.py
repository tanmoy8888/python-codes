def check_set():
   my_set_1 = {1,2,3,4,4,5,5}
   my_set_2 = {3,3,4,4,5,5}
   print(my_set_1.issuperset(my_set_2))
def main():
    check_set()

if __name__ == "__main__":
    main()