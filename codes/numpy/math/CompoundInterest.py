import math

def main():
    print("Compound interest is :: ",compound(100, 4, 10))

def compound(principal,rate,time):
    amount = principal * math.pow((1 + rate), time)
    interest = amount - principal
    return interest
if __name__ == "__main__":
    main()