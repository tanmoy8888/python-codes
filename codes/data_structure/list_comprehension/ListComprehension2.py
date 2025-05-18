

def list_print():
    lst1 = [1,2,3,4]
    lst2 = ['a','b','c','d']
    combine_list = [[i,j] for i in lst1 for j in lst2]
    return combine_list
def main():
    print(list_print())

if __name__ == "__main__":
    main()
