def check_set():
   my_set_1 = {1,2,3,4,5,5}
   print(my_set_1)
   my_set_1.add(6)
   print(my_set_1)
   my_set_1.remove(6)
   print(my_set_1)
   my_set_1.discard(6)
   print(my_set_1)
def main():
    check_set()

if __name__ == "__main__":
    main()