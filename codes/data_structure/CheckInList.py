def list_print():
    names = ["Aarav", "Aditi", "Arjun", "Diya", "Kabir", "Kiara", "Rohan", "Sanya", "Vedant", "Zara", "Aryan", "Ananya", "Krishna", "Priya", "Vikram"]
    found = False
    for s in names:
        if s == "Dhawal":
            print("Name is present")
            found = True
            break
    if not found:
        print("Name is not present")

def main():
    list_print()


if __name__ == "__main__":
    main()
