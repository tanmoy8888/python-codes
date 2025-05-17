def list_print():
    list = []
    for i in range(1, 51):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            list.append(i)
    print(list)


def main():
    list_print()


if __name__ == "__main__":
    main()
