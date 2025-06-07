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
if __name__ == "__main__":
    main()