# Given two characters, c1 and c2, print all the alphabets starting from c1 to c2, separated by a space, in a single line.
# Do not print a newline yourself, as it will be handled by the driver code.

def alphabets(c1, c2):
    alphabets_list = "abcdefghijklmnopqrstuvwxyz"
    first_position = 0
    last_position = 0
    count = 0
    for i in alphabets_list:
        print("i" ,i)
        if c1 == i and c2 == i:
            first_position = count
            print("first_position",first_position)

            last_position = count
            print("last_position", last_position)

            count = count + 1
    return alphabets_list[first_position, last_position + 1]

def main():
    alphabets('a', 'd')

if __name__ == "__main__":
    main()
