def main():

  for i in range(1,51):
      for j in range(2,i):
          if(i%j == 0):
              break
          else:
              print("This is prime" ,j)


if __name__ == "__main__":
    main()