def main():
    user_input = int(input("Enter a integer , "))
    if user_input <= 1:
        print("This is prime number ")
    else:
        counter = True
        for i in range(2, user_input):
            if user_input % i == 0:
                counter = False
                print("This is prime number")
                break
            else:
                print("This is NOT a prime number")


if __name__ == "__main__":
    main()
