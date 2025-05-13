# Given a string s, you need to reverse it.

def reverseString(s):
  reverse_string = ""
  for i in s:
      reverse_string = i+reverse_string
  return reverse_string

def main():
    print(reverseString("World"))

if __name__ == "__main__":
    main()
