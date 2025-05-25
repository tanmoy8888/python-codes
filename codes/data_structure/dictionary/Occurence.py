def check_dict():
  numbers = [1,2,2,3,3,3,4,4,4,4]
  my_dict = {}
  for i in numbers:
      if i in my_dict:
          my_dict[i]+=1
      else:
          my_dict[i]=1
  print(my_dict)
def main():
    check_dict()


if __name__ == "__main__":
    main()