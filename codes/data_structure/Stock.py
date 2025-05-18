def calculate():
   inventory = ["Maruti","Audi","Mercedes","BMW","Toyota"]
   inventory.append("Tata")
   print("New inventory 'Tata' added",inventory)
   inventory.remove("Maruti")
   print("Existing inventory 'Maruti' removed", inventory)

   if "Audi" in inventory:
       print("Car exists in inventory")
   else:
       print("Car does not exists in inventory")
def main():
    calculate()

if __name__ == "__main__":
    main()
