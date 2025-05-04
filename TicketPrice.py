def main():
    age = int(input("Enter your age "))
    student = input("Are you a student Y/N ?")

    if age < 5:
        print("As age is less than 5 , ticket will be free")
    elif 5 <= age < 18:
        if student == 'Y':
            ticket_price = 200 -100
            print(f'As you are also a student you should get a discount , {ticket_price}')
        else:
            print(f'As you are also a not student you should not get a discount , 200')
    elif 18 <= age <= 60:
        if student == 'Y':
            ticket_price = 200 - 100
            print(f'As you are also a student you should get a discount , {ticket_price}')
        else:
            print(f'As you are also a not student you should not get a discount , 200')


if __name__ == "__main__":
    main()