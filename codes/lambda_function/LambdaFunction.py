import math

def main():
    print(add(2, 3))
    # Lambda Function
    # Require a lambda keyword
    addition = lambda a, b: a + b
    print(addition(4,4))
    sqrt = lambda x:math.sqrt(x)
    even_or_odd = lambda x: x%2==0
    print(sqrt(16))
    print("Checking even or odd :: ",even_or_odd(6))
def add(a,b):
    return a+b
if __name__ == "__main__":
    main()