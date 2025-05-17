def list_print():
    list = []
    for i in range(1, 6):
            list.append(i)
    print(list[::-1])


def main():
    list_print()


if __name__ == "__main__":
    main()
