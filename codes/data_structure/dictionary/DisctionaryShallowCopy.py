def check_dict():
    my_dict_1 = ([(1, "abc"), (2, "def"), (3, "ghi")])
    my_dict_2 = my_dict_1
    print(my_dict_1)
    my_dict_2[0] = "ABCDE"
    print(my_dict_2)

def main():
    check_dict()

if __name__ == "__main__":
    main()
