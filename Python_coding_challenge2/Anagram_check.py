# This program checks whether two strings are anagrams

# Take input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Sort both strings and compare
if sorted(s1) == sorted(s2):
    print(True)
else:
    print(False)

# Output:
# Enter first string: listen
# Enter second string: silent
# True