
def main():
    print(add(2, 3))
    # Lambda Function
    # Require a lambda keyword
    addition = lambda a, b: a + b
    print(addition(4,4))
def add(a,b):
    return a+b
if __name__ == "__main__":
    main()