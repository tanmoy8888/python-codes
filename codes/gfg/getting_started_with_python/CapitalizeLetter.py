# Given a string s, you need to perform the following operation.
#
# 1. Capitalize the first letter and print.
#
# 2. Convert the whole string to uppercase and print.

def changeCase(s):
 print(s.capitalize())
 print(s.upper())

def main():
 changeCase("Hello World")
if __name__ == "__main__":
    main()