def main():
    lst = [1,2,3,4,5]
    print(list(map(lambda x: x * x, lst)))
    # Addition of two list
    list_1 = [1,2,3,4]
    list_2 = [5,6,7,8]
    print(list(map(lambda x, y: x + y, list_1, list_2)))
def add(a,b):
    return a+b
if __name__ == "__main__":
    main()