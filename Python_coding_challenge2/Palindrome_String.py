# This program checks whether a string is palindrome or not

# Take input
s = input("Enter string: ")

# Reverse string using slicing
rev = s[::-1]

# Compare original and reversed string
if s == rev:
    print("Yes")
else:
    print("No")

# Output:
# Enter string: madam
# Yes