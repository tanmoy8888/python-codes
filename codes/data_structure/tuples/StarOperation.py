def star_operation():
   tuple_pack =[1,2,3,4,5]
   a,*b,c = tuple_pack
   print(a)
   print(b)
   print(c)
def main():
    star_operation()

if __name__ == "__main__":
    main()
