def main():
    user_input = input("Enter a String , ")
    print("You entered " , user_input)
    rev_str = ""
    for i in user_input:
        rev_str = i + rev_str

    print("Sum of total number is : ", rev_str)

    if user_input == rev_str:
        print("This is palindrome")
    else:
        print("This is NOT a palindrome")

if __name__ == "__main__":
    main()