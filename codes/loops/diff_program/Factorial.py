def main():
    user_input = int(input("Enter a String , "))
    print("You entered " , user_input)
    factorial = 1
    for i in range(user_input,1,-1):
        factorial = factorial * i

    print("Factorial is : ", factorial)

if __name__ == "__main__":
    main()