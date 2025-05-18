def calculate():
    car = input("Enter a car brand , ")
    inventory = ["Maruti", "Audi", "Mercedes", "BMW", "Toyota"]
    #[car for car in inventory if car in inventory print("Car exists in iventory") else print("car does not exists in inventory")]
    var = [car for car in inventory if car in inventory]
    if var:
        print("Car exists in inventory")
    else:
        print("Car does not exists in inventory")
def main():
    calculate()

if __name__ == "__main__":
    main()
