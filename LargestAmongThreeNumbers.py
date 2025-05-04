def main():
    a = int(input("Enter first number "))
    print( f' [a] is first number ,  its value is {a}')
    b = int(input("Enter second number "))
    print(f' [b] is first number ,  its value is {b}')
    c = int(input("Enter third number "))
    print(f' [c] is first number ,  its value is {c}')

    if a >= b and a >= c:
        print(f' [a] is largest number ,  its value is {a}')
    elif b >= a and b >= c:
        print(f' [b] is largest number ,  its value is {b}')
    else:
        print(f' [c] is largest number ,  its value is {c}')


if __name__ == "__main__":
    main()