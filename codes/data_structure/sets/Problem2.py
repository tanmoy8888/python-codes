def check_set():
   text= "hi everyone i am from gfg data science , data analytics , data engineering , i am teaching in this batch , thanks everyone"
   my_set = set()
   for s in text.split(" "):
       my_set.add(s)
   print(my_set)
   print(set(text.split(" ")))
def main():
    check_set()

if __name__ == "__main__":
    main()