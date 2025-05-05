def main():
    user_input = int(input("Enter a natural number , "))
    total = 0
    for i in range(user_input+1):
        total = total+i
    print("Sum of total number is : " ,total)



if __name__ == "__main__":
    main()