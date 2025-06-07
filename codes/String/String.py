import string

def main():
    print(string.digits)
    x = "data science"
    print(x.upper())
    print(x.lower())
    print(x.capitalize())
    print(x.title())

    y = "123"
    print("Is y is a digit :: ",y.isdigit())
    # Check space
    z = ' '
    print(z.isspace())
    a = " "
    print(a.isspace())
    # Reverse String
    print("Printing String in reverse :: ",x[::-1])


if __name__ == "__main__":
    main()