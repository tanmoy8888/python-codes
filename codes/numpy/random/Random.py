import random

def main():
    print(random.random())
    print(random.randint(1,6))
    print(random.choice([1, 4, 5, 6, 9, 2, 7]))
    print(random.sample([1, 6, 2, 8, 3, 9, 4], 3))

if __name__ == "__main__":
    main()