# Given a string s, you need to slice it so that the output is a substring
# that contains all the characters except first and last.
# The length of the s will be greater than 2.

def slice_string(s):
    length = 0
    count = 0
    slice_input = ""
    for i in s:
        length = length+1
    for i in s:
        count = count+1
        if count != 1 and count != length:
            slice_input = slice_input +i
    return slice_input
def main():
    print(slice_string("World"))


if __name__ == "__main__":
    main()
