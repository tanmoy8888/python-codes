import datetime

def main():
    print(datetime.datetime.now())
    print(datetime.datetime(2025,6,7,1,8,10))
    # Format date time
    print(datetime.datetime.now().strftime("%d:%m:%y:%H:%M:%S"))
    print(datetime.datetime.now().strftime("%d:%m:%y"))
if __name__ == "__main__":
    main()