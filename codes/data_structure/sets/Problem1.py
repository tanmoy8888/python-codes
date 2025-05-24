def check_set():
   my_list = [2,5,4,6,7,8,8,6,7,4]
   my_set = set()
   for i in my_list:
       my_set.add(i)
   print(my_set)
def main():
    check_set()

if __name__ == "__main__":
    main()