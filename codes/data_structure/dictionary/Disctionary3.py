def check_set():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "year": 2020
    }
    print(thisdict)
    print(thisdict.keys())
    for k,v in thisdict.items():
        print(k, " : ", v)

def main():
    check_set()


if __name__ == "__main__":
    main()
