def check_dict():
  my_dict_1 = {"Amit": 10, "Rahul": 11}
  a = [my_dict_1.get("Amit") in my_dict_1]
  print(a)


def main():
    check_dict()


if __name__ == "__main__":
    main()
